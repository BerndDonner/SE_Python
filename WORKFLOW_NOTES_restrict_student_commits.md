# Notizen zum Workflow „Restrict student commits“

> Diese Datei dokumentiert Zweck, Design-Entscheidungen und Historie des GitHub-Actions-Workflows  
> `Restrict student commits`.  
> Sie ist vor allem dafür gedacht, die ganze Vorgeschichte später schnell an eine KI „anzudocken“.

---

## 1. Ziel des Workflows

Der Workflow soll in Schüler-Repos sicherstellen:

- Jeder Schüler arbeitet **nur in seinem eigenen Unterordner**:
  - Ordnername **muss exakt dem GitHub-Login entsprechen** (`${actor}/`).
- Zusätzlich global erlaubt:
  - `common/` – gemeinsam nutzbarer Ordner  
  - `shared/` – weiterer gemeinsamer Ordner  
  - `README.md` – allgemeine Projekt-Info
- Alle anderen Pfade sind für normale Schüler **verboten**.

Sobald ein Commit (Push / Pull Request / manuell angestoßen) Dateien außerhalb dieser erlaubten Bereiche verändert, schlägt der Workflow **fehlerhaft** fehl.

Spezialfall:

- Benutzer `BerndDonner` (Lehrer) wird **explizit ausgenommen** – er darf überall Änderungen machen.

---

## 2. Wann läuft der Workflow?

```yaml
on:
  push:
  pull_request:
  workflow_dispatch:
```

### Events im Detail

- **`push`**
  - Normale Pushes der Schüler.
  - Hier wird typischerweise hart geprüft, ob sie nur im eigenen Ordner gearbeitet haben.

- **`pull_request`**
  - Gleiche Logik wie bei `push`.
  - Sinnvoll, wenn PRs z.B. auf einen gemeinsamen Branch gehen.

- **`workflow_dispatch`**
  - Manuelles Anstoßen über die GitHub-UI.
  - Zusätzliche Inputs:
    - `from_sha` – Start-Commit für den Vergleich (Default: `HEAD^`)
    - `to_sha` – Ziel-Commit für den Vergleich (Default: `HEAD`)
    - `actor` – GitHub-Login, dessen Pfade geprüft werden sollen (überschreibt `github.actor`)
  - Praktisch, um im Nachhinein bestimmte Diffs oder Schüler manuell zu prüfen.

---

## 3. Wichtige Umgebungsvariablen

Im Step `Verify changed file paths` werden folgende Umgebungsvariablen gesetzt:

- `GITHUB_EVENT_NAME` – Art des Events (`push`, `pull_request`, `workflow_dispatch`).
- `GITHUB_ACTOR` – GitHub-Login, der den Event ausgelöst hat.
- `GITHUB_REF_NAME` – Branch-Name.
- `EVENT_BEFORE` – `github.event.before`  
  - Bei `push`: SHA des vorherigen Commit-Zustands.
  - Bei neuem Branch / erstem Commit: 40× `0`.
- `EVENT_SHA` – `github.sha`  
  - SHA des neuen Commits / aktuellen Checkout-Status.
- `INPUT_FROM_SHA`, `INPUT_TO_SHA`, `INPUT_ACTOR`  
  - Manuelle Inputs für `workflow_dispatch`.

Diese Werte steuern, **welche Commits verglichen** werden und **welcher Benutzer-Ordner** gilt.

---

## 4. Locale / UTF-8 / Umlaute

### Problem (Historie)

- In älteren Versionen wurden Dateinamen mit Umlauten (z.B. `Übung_Ärger_Ökonom.py`) in der Ausgabe von `git diff` „kaputt“ angezeigt (`\303\234bung_...`).
- Das erschwert Debugging und kann theoretisch auch Pfadprüfungen stören.

### Lösung

Im Script werden explizit gesetzt:

```bash
export LANG=C.UTF-8
export LC_ALL=C.UTF-8
```

Und beim Git-Diff:

```bash
git -c core.quotepath=off diff ...
git -c core.quotepath=off diff-tree ...
```

- `C.UTF-8` → konsistente, UTF-8-fähige C-Locale.
- `core.quotepath=off` → Git zeigt Dateinamen mit Sonderzeichen lesbar an, nicht als escaped Byte-Sequenzen.

---

## 5. Checkout / History / fetch-depth

### Ausgangslage

Wir verwenden:

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0
```

- `fetch-depth: 0` = gesamte Branch-Historie wird geholt (nicht nur der neueste Commit).
- Das ist wichtig für **Diffs zwischen zwei SHA-Ständen**.

### Neues Problem (später aufgetreten)

Trotz `fetch-depth: 0` kam es bei folgendem Szenario zu:

```text
fatal: bad object <EVENT_BEFORE_SHA>
Error: Process completed with exit code 128.
```

Ursache:

- Ein Schüler (User 2) hat ein **Rebase + Force-Push** gemacht.
- `github.event.before` (`EVENT_BEFORE`) zeigt auf den **alten Branch-Tip**, der nach dem Force-Push nicht mehr durch die Branch-Refs referenziert wird.
- `actions/checkout` holt zwar die aktuelle Branch-History, aber **nicht automatisch solche „verwaisten“ Commits**.
- Folge: `git diff EVENT_BEFORE EVENT_SHA` schlägt mit „bad object“ fehl.

---

## 6. Commit-Vergleichslogik (aktuelle Version)

### 6.1 Grundidee

Wir brauchen eine **Liste der geänderten Dateien** (`$CHANGED`). Diese wird später für die Pfadprüfung verwendet.

Der Workflow geht dabei wie folgt vor:

#### A) `workflow_dispatch`

- Mit (optional) `from_sha` / `to_sha`:

```bash
FROM="$INPUT_FROM_SHA"
TO="$INPUT_TO_SHA"

[ -z "$TO" ] && TO="HEAD"
[ -z "$FROM" ] && FROM="${TO}^"

CHANGED=$(git -c core.quotepath=off diff --name-only "$FROM" "$TO")
```

- Damit kann man manuell beliebige Diffs prüfen.

#### B) `push` / `pull_request`

1. **Erster Commit / neuer Branch**

   Wenn `EVENT_BEFORE` nur Nullen enthält:

   ```bash
   CHANGED=$(git -c core.quotepath=off diff-tree --no-commit-id --name-only -r "$EVENT_SHA")
   ```

   → Es werden nur die Dateien des neuen Commits betrachtet.

2. **Normalfall (kein erster Commit)**

   Zuerst versuchen wir, den `EVENT_BEFORE`-Commit verfügbar zu machen:

   ```bash
   git fetch --no-tags origin "$EVENT_BEFORE" || true
   ```

   Danach prüfen wir:

   ```bash
   if git cat-file -e "$EVENT_BEFORE^{commit}" 2>/dev/null; then
       CHANGED=$(git -c core.quotepath=off diff --name-only "$EVENT_BEFORE" "$EVENT_SHA")
   else
       # Fallback ...
   fi
   ```

   Wenn der Commit trotzdem nicht existiert (z.B. nach Rebase/Force-Push):

   - **Fallback 1**: Datei-Liste direkt aus dem Push-Event lesen:

     ```bash
     if command -v jq >/dev/null 2>&1; then
       CHANGED=$(jq -r '.commits[]? | .added[]?, .modified[]?, .removed[]?' \
         "$GITHUB_EVENT_PATH" 2>/dev/null | sort -u)
     fi
     ```

   - **Fallback 2**: Notfalls nur den aktuellen Commit auswerten:

     ```bash
     if [ -z "$CHANGED" ]; then
       CHANGED=$(git -c core.quotepath=off diff-tree --no-commit-id --name-only -r "$EVENT_SHA")
     fi
     ```

Damit wird verhindert, dass der Workflow **nicht mehr mit Exit-Code 128** abbricht, wenn `EVENT_BEFORE` nicht verfügbar ist.  
**Wichtig:** In allen Fällen wird am Ende eine Liste von Dateipfaden in `$CHANGED` erzeugt.

---

## 7. Leere Diffs

Wenn `$CHANGED` leer ist (keine Dateien geändert):

```bash
if [ -z "$CHANGED" ]; then
  echo "✅ Keine geänderten Dateien gefunden."
  exit 0
fi
```

Der Workflow bricht dann **erfolgreich** ab.  
Das vermeidet unnötige Fehlermeldungen bei z.B. Events ohne relevante Änderungen.

---

## 8. Actor-Bestimmung & Lehrer-Ausnahme

### Actor-Bestimmung

```bash
actor="$GITHUB_ACTOR"
if [ "$GITHUB_EVENT_NAME" = "workflow_dispatch" ] && [ -n "$INPUT_ACTOR" ]; then
  actor="$INPUT_ACTOR"
fi
```

- Standard: `github.actor` (der User, der das Event ausgelöst hat).
- Bei `workflow_dispatch` kann `actor` manuell überschrieben werden:
  - Praktisch, um nachträglich „so zu tun“, als würden wir den Commit eines bestimmten Schülers prüfen.

### Lehrer-Ausnahme

```bash
if [ "$actor" = "BerndDonner" ]; then
  echo "🧑‍🏫 Lehrer erkannt – keine Pfadprüfung erforderlich."
  exit 0
fi
```

- Der Lehrer soll sich frei im Repo bewegen können (auch Actions, Configs usw. ändern).
- Diese Ausnahme ist bewusst hart codiert.

---

## 9. Pfad-Regex / erlaubte Bereiche

Nach dem Sammeln der geänderten Dateien in `$CHANGED` wird geprüft, ob alle in erlaubten Pfaden liegen.

### Erlaubte Präfixe

```bash
allowed_prefixes="^(${actor}/|common/|shared/|README\.md|$)"
```

Bedeutung:

- `^` – Beginn der Zeile
- `${actor}/` – persönlicher Ordner des jeweiligen GitHub-Users
- `common/` – gemeinsamer Ordner
- `shared/` – weiterer gemeinsamer Ordner
- `README\.md` – explizit dieses File in Repo-Root
- `$` – leere Zeile (zur Sicherheit, wenn `CHANGED` z.B. Trailing Newline hat)

### Prüfung

```bash
violations=$(echo "$CHANGED" | grep -Ev "$allowed_prefixes" || true)
```

- `grep -E` → Regex
- `-v` → wir sammeln **alles, was nicht passt** (also alle verbotenen Pfade).
- `|| true` → verhindert, dass `grep` durch Exit-Code 1 den Workflow killt, wenn es gar keine Zeilen findet.

Wenn `violations` **nicht leer** ist:

```bash
if [ -n "$violations" ]; then
  echo "❌ Commit enthält Dateien außerhalb deines Verzeichnisses!"
  echo "👤 Erlaubt ist nur: ${actor}/ (plus ggf. common/, shared/, README.md)"
  echo "🚫 Nicht erlaubte Dateien:"
  echo "$violations"
  exit 1
fi
```

→ Der Workflow schlägt fehl und listet die verbotenen Pfade auf.

---

## 10. Historie der wichtigsten Probleme & Fixes

### Problem 1: Umlaute / Encoding-Müll in Dateinamen

- Git-Ausgabe mit escaped Pfadnamen (`\303\234bung_...`).
- Debugging und Zuordnung zu realen Dateien erschwert.
- **Fix:** `LANG=C.UTF-8`, `LC_ALL=C.UTF-8`, `core.quotepath=off`.

### Problem 2: Zu „clevere“ Case-Insensitivity

- Zwischendurch gab es eine Version, die `actor` / Ordnernamen case-insensitive behandeln wollte.
- Das führte zu potenziell unerwartetem Verhalten (z.B. wenn Verzeichnis-Schreibweise nicht exakt zum Login passte).
- **Entscheidung:** Kein Case-Magic, **Ordnername muss exakt dem GitHub-Login entsprechen**.  
  -> Weniger Magie, klarere Regeln für Schüler.

### Problem 3: Event mit `EVENT_BEFORE == 000...0`

- Erster Commit / neuer Branch, kein echter „Vorher“-Commit.
- Frühe Versionen waren hier nicht robust genug.
- **Fix:** Sonderbehandlung:
  - `if EVENT_BEFORE == 000...0 → diff-tree nur auf HEAD (EVENT_SHA)`

### Problem 4 (aktuell): `fatal: bad object <EVENT_BEFORE>`

- Trat trotz `fetch-depth: 0` auf.
- Typischer Auslöser: **Rebase + Force-Push** eines Schülers.
- `EVENT_BEFORE` zeigt auf einen Commit, der nicht mehr per Branch-Ref erreichbar ist und
  daher beim normalen Fetch nicht ankommt.
- **Fix:**
  - Versuch, `EVENT_BEFORE` explizit zu fetchen: `git fetch origin "$EVENT_BEFORE"`.
  - Prüfung mit `git cat-file -e`.
  - Falls nicht vorhanden:
    - Fallback über `GITHUB_EVENT_PATH` (JSON) + `jq`.
    - Letzter Fallback: `diff-tree` nur auf `EVENT_SHA`.

Dadurch bricht der Workflow **nicht mehr mit Exit-Code 128** ab, sondern liefert immer eine sinnvolle Dateiliste.

---

## 11. Kurzfassung für „späteres KI-Onboarding“

Wenn du diese Datei in eine KI wirfst, hier das Wichtigste in einem Block:

- Workflow heißt **„Restrict student commits“**.
- Zweck:
  - Schüler dürfen nur in `${actor}/`, `common/`, `shared/` und `README.md` im Root ändern.
  - `actor` ist der GitHub-Login oder bei `workflow_dispatch` der `actor`-Input.
  - Lehrer `BerndDonner` ist ausgenommen.
- Events: `push`, `pull_request`, `workflow_dispatch`.
- Diffs:
  - `workflow_dispatch`: `from_sha`/`to_sha` oder default `HEAD^..HEAD`.
  - `push`/`pull_request`:
    - `EVENT_BEFORE` = Nullen → `diff-tree` auf `EVENT_SHA`.
    - Sonst: Versuch `git fetch origin EVENT_BEFORE`, dann
      - wenn Commit existiert → `git diff EVENT_BEFORE EVENT_SHA`,
      - sonst Fallback über `GITHUB_EVENT_PATH` (`jq`) bzw. `diff-tree EVENT_SHA`.
- Wichtige Einstellungen:
  - `fetch-depth: 0` bei `actions/checkout@v4`.
  - `LANG=C.UTF-8`, `LC_ALL=C.UTF-8`, `core.quotepath=off`.
- Pfadprüfung:
  - Regex: `^(${actor}/|common/|shared/|README\.md|$)`
  - Verletzungen → Workflow `exit 1`.

# 🐍 Softwareentwicklung in Python

Dieses Repository enthält Unterrichtsmaterialien, Beispielcode und Übungsaufgaben für das Fach **Softwareentwicklung in Python**.

Es handelt sich bewusst um ein **Unterrichts-Repository mit Wegwerf-Code**:
- Der Code muss nicht „perfekt“ oder langfristig wartbar sein.
- Wichtiger sind: Ausprobieren, Fehler machen, Zusammenhänge verstehen.
- Die Git-History darf bei Bedarf aufgeräumt und umgeschrieben werden.

---

## ⚙️ Projektstruktur

Vereinfachte Übersicht über die wichtigsten Verzeichnisse:

```text
SE_Python/
 ├── _config/                      → Zentrale Projektkonfiguration
 ├── Datentypen/                   → Übungen zum Thema Datentypen
 ├── Listen/                       → Übungen zu Listen / Sequenzen
 ├── Zahlen/                       → Übungen zu Zahlen / Rechnen
 ├── Uebung01/, Uebung07_01/, ...  → Weitere Übungsblöcke
 ├── Spielwiese/                   → Unterrichtsvorbereitung / Experimente (Herr Donner)
 ├── .github/workflows/restrict.yml→ GitHub Action zur Commit-Prüfung
 ├── .vscode/                      → Lokale VS-Code-Einstellungen (optional)
 ├── flake.nix, flake.lock         → Nix-Umgebung (nur für den Lehrer relevant)
 ├── WORKFLOW_NOTES_restrict_student_commits.md → Hintergrund zur GitHub-Action
 └── README.md                     → Diese Datei
```

### Kurzbeschreibung der wichtigsten Ordner

- `_config/`
  - `gitconfig` – zentrale Git-Konfiguration (siehe unten)
  - `launch.json` – VS-Code-Debugkonfiguration
  - `settings.json` – empfohlene VS-Code-Einstellungen
  - `config.yaml` – interne Konfiguration / Notizen für den Unterricht

- `Datentypen/`, `Listen/`, `Zahlen/`, `Uebung…/`
  - Übungen und Aufgaben für die Schüler (meist mit `main.py`).

- `Spielwiese/`
  - Test- und Beispielcode aus der Unterrichtsvorbereitung.
  - Hier probiert der Lehrer neue Aufgaben und Beispiele aus.

- `.github/workflows/restrict.yml`
  - GitHub-Action, die Schüler-Commits prüft (z. B. auf erlaubte Pfade).
  - Details stehen in `WORKFLOW_NOTES_restrict_student_commits.md`.

- `.vscode/`
  - Lokale VS-Code-Einstellungen, die auf diesem Rechner bereits eingerichtet sind.
  - Schüler können diese Einstellungen übernehmen, müssen aber nicht.

- `flake.nix`, `flake.lock`
  - Nix-Definitionen für eine reproduzierbare Entwicklungsumgebung (Linux / NixOS).
  - Für Schüler in der Regel uninteressant – der Unterricht funktioniert auch ohne Nix.

---

## 🧩 Einheitliche Git-Konfiguration

Damit alle denselben **Git-Workflow** verwenden, gibt es eine zentrale Konfigurationsdatei:

```text
_config/gitconfig
```

### Einbindung in dein lokales Repository

Im Projektordner (dort, wo auch `.git` liegt) **einmalig** ausführen:

```bash
git config --local include.path "../_config/gitconfig"
```

> Hinweis:  
> Der Befehl ergänzt deine lokale `.git/config`.  
> Danach gelten die empfohlenen Git-Einstellungen automatisch für dieses Repository.

---

## 🧭 Git-Workflow in diesem Unterrichtsrepo

Die zentrale `gitconfig` unterstützt einen **einfachen, linearen Workflow** ohne unnötige Merge-Commits.

Wichtige Einstellungen:

| Bereich                       | Zweck                                                                 |
|------------------------------|-----------------------------------------------------------------------|
| `pull.rebase = true`         | Verhindert unübersichtliche Merge-Commits beim `git pull`            |
| `pull.ff = only`             | Erlaubt nur Fast-Forward-Updates                                     |
| `rebase.autoStash = true`    | Sichert lokale Änderungen während eines Rebase automatisch           |
| `rerere.enabled = true`      | Git merkt sich gelöste Konflikte (nützlich beim Üben)                |
| `merge.conflictStyle = diff3`| Zeigt Konflikte übersichtlicher an (Basis + beide Seiten)           |

### Hinweis zu Konflikten

Frühere Varianten hatten:

```ini
[rebase]
    autoMergeStrategy = ours
```

Das wurde **bewusst entfernt**, weil:
- „ours“ bei Konflikten still die **lokale Seite bevorzugt**  
- und damit Änderungen der Gegenseite verwerfen kann, ohne dass man den Konflikt sieht.

Im Unterricht ist es sinnvoller:
- Konflikte zu sehen,
- sie einmal sauber zu lösen,
- und dann von `rerere` profitieren, wenn derselbe Konflikt noch einmal auftaucht.

---

## 🧙‍♂️ Git-Aliase in diesem Projekt

### `git lg` – History im Überblick

In `_config/gitconfig` ist definiert:

```ini
[alias]
    lg = log --oneline --graph --decorate --all
```

Nutzung:

```bash
git lg
```

Zeigt den Commit-Verlauf kompakt als Graph (alle Branches).  
Gut geeignet, um ein Gefühl für die Git-History zu bekommen.

---

## 🔀 Branch-Regeln im Unterricht

Für dieses Unterrichtsrepo gilt typischerweise:

- `master` ist der zentrale Lehrer-Branch.
- Jeder Schüler arbeitet auf **einem eigenen Branch**, idealerweise:
  - Branchname = dein GitHub-Login, z. B. `Anian`, `Antonia`, `Thomas`, …
- Auf `master` wird nicht direkt entwickelt.

Typisches Vorgehen für Schüler:

```bash
# Einmalig eigenen Branch anlegen (falls noch nicht vorhanden)
git checkout -b MeinLogin
git push -u origin MeinLogin

# Danach immer wieder:
# Änderungen machen, committen, pushen
git status
git add .
git commit -m "Mein Kommentar"
git push
```

---

## ⬆️ `git upmaster` – eigenen Branch aufräumen und aktualisieren

In `_config/gitconfig` ist ein Alias `upmaster` definiert.  
Er ist **explizit dafür gedacht**, dass Schüler ihren **eigenen Branch** auf den aktuellen Stand bringen.

Vereinfacht gesagt:  
> „Mach meinen Branch sauber, zieh ihn auf den neuesten Stand und schieb ihn zurück zum Server.“

Der Alias sieht (gekürzt) so aus:

```ini
[alias]
    upmaster = "!f(){ set -e; \
      b=$(git rev-parse --abbrev-ref HEAD); \
      if [ \"$b\" = master ] || [ \"$b\" = main ]; then \
        echo \"ERROR: upmaster nicht auf '$b' ausfuehren.\"; exit 1; \
      fi; \
      u=$(git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null) || { \
        echo \"ERROR: Kein Upstream gesetzt. Setze ihn mit: git push -u origin $b\"; exit 1; }; \
      if [ \"$u\" != \"origin/$b\" ]; then \
        echo \"ERROR: Upstream ist '$u', erwartet 'origin/$b'.\"; exit 1; \
      fi; \
      git fetch origin; \
      git rebase @{u}; \
      git rebase origin/HEAD; \
      git push --force-with-lease origin HEAD:refs/heads/$b; \
    }; f"
```

### Was macht `git upmaster` genau?

Angenommen, du bist auf deinem eigenen Branch `MeinLogin`:

```bash
git upmaster
```

Dann passiert:

1. `git fetch origin`  
   → Holt alle aktuellen Änderungen vom Server.

2. `git rebase @{u}`  
   → Baut deine lokalen Commits auf den Stand deines Remote-Branches `origin/MeinLogin`.  
   Nützlich, wenn du z. B. an zwei Rechnern arbeitest.

3. `git rebase origin/HEAD`  
   → Baut deinen Branch zusätzlich auf den aktuellen Stand des Hauptbranches (`master` oder `main`).

4. `git push --force-with-lease origin HEAD:refs/heads/MeinLogin`  
   → Schiebt den aufgeräumten Verlauf zurück zu `origin/MeinLogin`, ohne fremde Änderungen blind zu überschreiben.

### Regeln für `git upmaster`

- ✅ Verwende `upmaster` **nur auf deinem eigenen Branch**, auf dem nur du arbeitest.
- ✅ Dein Branch sollte einen Upstream haben: `origin/<deinBranch>`.
- ❌ **Nie** auf `master` oder `main` ausführen (wird zusätzlich vom Alias blockiert).
- ❌ Nicht auf Branches benutzen, die mehrere Personen gemeinsam verwenden.

Für dieses Unterrichtsrepo mit Wegwerf-Code ist das Umschreiben der History völlig in Ordnung und hilft, den Verlauf übersichtlich zu halten.

---

## 💡 VS Code-Einstellungen

Im Ordner `_config` sind empfohlene VS-Code-Einstellungen hinterlegt:

| Datei          | Zweck                                                       |
|----------------|-------------------------------------------------------------|
| `launch.json`  | Startet den Python-Debugger direkt für die aktuelle Datei   |
| `settings.json`| Automatisches Speichern, Formatieren beim Speichern, Git-Optimierungen |

Wer möchte, kann diese Dateien nach `.vscode/` kopieren:

```bash
mkdir -p .vscode
cp _config/launch.json _config/settings.json .vscode/
```

VS Code erkennt die Einstellungen dann automatisch beim Öffnen des Projekts.

---

## 🧰 Voraussetzungen

- Python ≥ 3.10  
- Git installiert  
- VS Code mit Python-Erweiterung (empfohlen)

---

## 📚 Lizenz und Nutzung

Dieses Repository darf im Unterricht frei genutzt und angepasst werden.  
Es ist für Lernzwecke gedacht und nicht als Produktionscode.

---

© 2026 Bernd Donner – Unterrichtsprojekt *Softwareentwicklung in Python*

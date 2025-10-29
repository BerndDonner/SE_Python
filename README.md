# 🐍 Softwareentwicklung in Python

Dieses Repository enthält Unterrichtsmaterialien, Beispielcode und Übungsaufgaben für das Fach **Softwareentwicklung in Python**.

---

## ⚙️ Projektstruktur

```
📁 SE_Python/
 ┣ 📁 _config/           → Zentrale Projektkonfiguration
 ┃ ┣ 🧩 gitconfig        → Einheitliche Git-Einstellungen
 ┃ ┣ 🧠 launch.json      → VS Code Debug-Konfiguration
 ┃ ┗ ⚙️ settings.json    → Empfohlene VS Code-Einstellungen
 ┣ 📁 src/               → Beispielcode und Übungsaufgaben
 ┣ 📁 docs/              → Begleitende Unterlagen (z. B. PDFs, Markdown)
 ┗ 📄 README.md          → Diese Datei
```

---

## 🧩 Einheitliche Git-Konfiguration

Damit alle denselben **Git-Workflow** nutzen, enthält das Projekt eine zentrale Konfigurationsdatei:

```
_config/gitconfig
```

### 📋 Einbindung in dein lokales Repository

Führe diesen Befehl **einmalig im Projektordner** aus:

```bash
git config --local include.path "../_config/gitconfig"
```

> ⚠️ **Hinweis:**  
> Der Befehl ergänzt deine lokale `.git/config`.  
> Danach gelten die im Projekt empfohlenen Git-Regeln automatisch.

---

## 🧭 Git-Workflow

Diese Konfiguration sorgt für einen sauberen, linearen Verlauf ohne Merge-Commits.

| Bereich        | Zweck |
|----------------|-------|
| `pull.rebase = true` | Verhindert unübersichtliche Merge-Commits |
| `pull.ff = only` | Nur Fast-Forward-Updates erlaubt |
| `rebase.autoStash = true` | Zwischenspeichern lokaler Änderungen |
| `rerere.enabled = true` | Git merkt sich gelöste Konflikte |
| `merge.conflictStyle = diff3` | Zeigt Konflikte übersichtlich |
| `rebase.autoMergeStrategy = ours` | Bevorzugt lokale Änderungen |

---

## 🧙‍♂️ Git-Aliase

| Alias | Befehl | Zweck |
|--------|---------|-------|
| `git lg` | `git log --oneline --graph --decorate --all` | Übersichtliche Verlaufsgrafik |
| `git upmaster` | `git fetch origin && git rebase origin/master && git push --force-with-lease` | Aktualisiert und synchronisiert den `master`-Branch |

> 🔹 `git upmaster` ist nur für Lehrkräfte oder Maintainer gedacht.  
> 🔹 Schüler arbeiten in eigenen Branches und verwenden `git push`.

---

## 💡 VS Code-Einstellungen

Im Ordner `_config` sind empfohlene VS Code-Voreinstellungen hinterlegt:

| Datei | Zweck |
|--------|--------|
| `launch.json` | Startet den Python-Debugger direkt für die aktuelle Datei |
| `settings.json` | Automatisches Speichern, Formatieren beim Speichern, Git-Optimierungen |

Damit VS Code diese Einstellungen automatisch erkennt, müssen die Dateien in einen Ordner namens **`.vscode/`** im Projektstamm kopiert werden:

```bash
cp _config/launch.json _config/settings.json .vscode/
```

> 💡 Danach erkennt VS Code die Einstellungen beim Öffnen des Projekts automatisch.

---

## 🧰 Voraussetzungen

- Python ≥ 3.10  
- Git installiert  
- VS Code mit Python-Erweiterung (empfohlen)

---

## 📚 Lizenz und Nutzung

Dieses Repository darf frei genutzt und geteilt werden.  
Es wurde für den Unterricht entwickelt, steht aber auch allen Interessierten offen.

---

© 2025 Bernd Donner – Unterrichtsprojekt *Softwareentwicklung in Python*


Das ist super wichtig

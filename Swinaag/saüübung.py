# ============================================================
# CLI-MEMORY – GESAMTPROGRAMM
# Basisprogramm + alle Zusatzaufgaben
# ============================================================

import random
import string
import time
import math
import os

# ------------------------------------------------------------
# Exception für Spielabbruch
# ------------------------------------------------------------
class SpielAbbruch(Exception):
    pass


# ------------------------------------------------------------
# GridView – Darstellung des Spielfelds
# ------------------------------------------------------------
class GridView:

    def __init__(self, anzahl_paare: int, anzahl_spalten: int) -> None:
        self.anzahl_karten = anzahl_paare * 2
        self.anzahl_spalten = anzahl_spalten
        self.anzahl_zeilen = (self.anzahl_karten + anzahl_spalten - 1) // anzahl_spalten

        zeilen_raw = [str(i) for i in range(self.anzahl_zeilen)]
        spalten_raw = list(string.ascii_uppercase[:anzahl_spalten])

        self.zeilen_header = [z.rjust(2) for z in zeilen_raw]
        self.spalten_header = [s.rjust(2) for s in spalten_raw]

        coords = [x + y for y in zeilen_raw for x in spalten_raw]
        self.position = {pos: i for i, pos in enumerate(coords[:self.anzahl_karten])}

    def get_index(self, pos: str):
        return self.position.get(pos)

    def render(self, karten):
        os.system("cls" if os.name == "nt" else "clear")
        lines = ["  " + " ".join(self.spalten_header)]
        for y in range(self.anzahl_zeilen):
            zeile = self.zeilen_header[y] + " "
            zeile += " ".join(karten[y * self.anzahl_spalten:(y + 1) * self.anzahl_spalten])
            lines.append(zeile)
        return "\n".join(lines)


# ------------------------------------------------------------
# Karte
# ------------------------------------------------------------
class Karte:

    def __init__(self, symbol: str, rueckseite: str) -> None:
        self.symbol = symbol
        self.rueckseite = rueckseite
        self._aufgedeckt = False

    def aufdecken(self):
        self._aufgedeckt = True

    def zudecken(self):
        self._aufgedeckt = False

    def aufgedeckt(self):
        return self._aufgedeckt

    def sichtbar(self):
        return self.symbol if self._aufgedeckt else self.rueckseite

    def vergleichen(self, andere):
        return self.symbol == andere.symbol


# ------------------------------------------------------------
# Memory-Spiel
# ------------------------------------------------------------
class Memory:

    def __init__(self, vorderseiten, rueckseiten):
        self.stapel = []
        for r in rueckseiten:
            for v in vorderseiten:
                self.stapel.append(Karte(v, r))

        random.shuffle(self.stapel)

        paare = len(vorderseiten)
        spalten = math.ceil(math.sqrt(paare * 2))
        self.grid = GridView(paare, spalten)

        self.history = []  # Undo-History

    def spielfeld(self):
        sicht = [k.sichtbar() for k in self.stapel]
        print(self.grid.render(sicht))

    def undo(self):
        if not self.history:
            print("↩️ 📜 Kein Zug zum Rückgängigmachen!")
            time.sleep(1.5)
            return
        i, j = self.history.pop()
        self.stapel[i].zudecken()
        self.stapel[j].zudecken()
        print("↩️ 🕘 Letzter Zug rückgängig gemacht!")
        time.sleep(1.5)

    def frage_zug(self):
        while True:
            self.spielfeld()
            try:
                raw = input("⌨️ Zwei Karten (A0 B1), undo oder quit: ").strip()
            except KeyboardInterrupt:
                raise SpielAbbruch()

            if raw.lower() in ("quit", "exit"):
                raise SpielAbbruch()

            if raw.lower() == "undo":
                self.undo()
                continue

            try:
                a, b = raw.split()
            except ValueError:
                print("⚠️ Bitte genau zwei Koordinaten eingeben!")
                time.sleep(1.5)
                continue

            i = self.grid.get_index(a.upper())
            j = self.grid.get_index(b.upper())

            if i is None or j is None:
                print("🚧 ❓ Ungültige Koordinaten!")
                time.sleep(1.5)
                continue

            if i == j:
                print("🪞 ♻️ Zwei verschiedene Karten wählen!")
                time.sleep(1.5)
                continue

            if self.stapel[i].aufgedeckt() or self.stapel[j].aufgedeckt():
                print("👀 🔁 Karte bereits aufgedeckt!")
                time.sleep(1.5)
                continue

            return i, j

    def spielen(self):
        try:
            while any(not k.aufgedeckt() for k in self.stapel):
                i, j = self.frage_zug()
                self.stapel[i].aufdecken()
                self.stapel[j].aufdecken()
                self.spielfeld()

                if self.stapel[i].vergleichen(self.stapel[j]):
                    print("🎯 🎉 Paar gefunden!")
                else:
                    print("💩 🙈 Kein Paar!")
                    self.history.append((i, j))
                    time.sleep(1.5)
                    self.stapel[i].zudecken()
                    self.stapel[j].zudecken()

                time.sleep(1.5)

            print("🏆 🏁 Glückwunsch! Alle Paare gefunden!")
        except SpielAbbruch:
            print("🛑 🚪 Spiel beendet. 👋")
    class Zug:
        def __init__


# ------------------------------------------------------------
# Emoji-Kataloge (Auswahl-Aufgaben)
# ------------------------------------------------------------
EMOJI_FRONT = {
    "tiere": ("🐍", "🐢", "🐸", "🦊", "🐙", "🦉"),
    "essen": ("🍕", "🍔", "🍟", "🍣", "🍩", "🍎"),
    "technik": ("💾", "💿", "📟", "📺", "🖥️", "⌨️"),
    "dinge": ("🎲", "🎯", "🧩", "🧠", "🔧", "🔑")
}

RUECKSEITEN = [
    ("⬛", "⬜"),
    ("🟦", "🟥"),
    ("🟩", "🟨"),
    ("🟪", "🟧"),
    ("◆", "◇"),
    ("■", "□"),
    ("▲", "△"),
    ("●", "○")
]


# ------------------------------------------------------------
# Auswahlfunktionen
# ------------------------------------------------------------
def waehle_vorderseiten() -> tuple[str, str, str, str, str, str]:
    while True:
        print("👉 Wähle eine Kategorie für die Vorderseiten:")
        for key in EMOJI_FRONT:
            print(" -", key)
        auswahl: str = input("⌨️ Eingabe: ").strip().lower()
        if auswahl in EMOJI_FRONT:
            print("✅ Kategorie gewählt:", auswahl)
            return EMOJI_FRONT[auswahl]
        else:
            print("⚠️ ❓ Ungültige Auswahl!")


def waehle_rueckseiten() -> tuple[str, str]:
    while True:
        print("👉 Wähle ein Rückseiten-Paar:")
        for i, pair in enumerate(RUECKSEITEN, start=1):
            print(f" {i}: {pair[0]} {pair[1]}")
        try:
            auswahl = int(input("⌨️ Nummer: "))
            if 1 <= auswahl <= len(RUECKSEITEN):
                print("✅ Rückseite gewählt:", RUECKSEITEN[auswahl - 1])
                return RUECKSEITEN[auswahl - 1]
            else:
                print("⚠️ ❓ Zahl außerhalb des Bereichs!")
        except ValueError:
            print("⚠️ ❌ Bitte eine Zahl eingeben!")


# ------------------------------------------------------------
# Programmstart
# ------------------------------------------------------------
vorderseiten: tuple[str, str, str, str, str, str] = waehle_vorderseiten()
rueckseiten: tuple[str, str] = waehle_rueckseiten()
spiel: Memory = Memory(vorderseiten, rueckseiten)
spiel.spielen()

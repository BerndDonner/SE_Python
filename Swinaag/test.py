# ------------------------------------------------------------
# 🧩 Emoji-Katalog (für die Prüfung)
# ------------------------------------------------------------
# ✅ Vorderseiten (Karten-Symbole) – gut unterscheidbar im CLI:
# Tiere:     🐍 🐢 🐸 🦊 🐙 🦄 🦖 🐝 🦉 🐧 🦁 🐳
# Essen:     🍕 🍔 🍟 🍣 🍩 🍪 🍎 🍉 🍓 🍌 🍇 🥨
# Technik:   💾 💿 📟 📺 🖥️ ⌨️ 🖱️ 🔌 🔋 📡 🛰️ 🧲
# Dinge:     🎲 🎯 🧩 🧠 🧪 🧯 🔧 🪛 🧱 🧭 🔑 🏆
#
# 🎴 Rückseiten (2 Stück pro Spiel) – klare Paare:
# Blöcke:    ("⬛", "⬜")  ("🟦", "🟥")  ("🟩", "🟨")  ("🟪", "🟧")
# Formen:    ("◆", "◇")  ("■", "□")  ("▲", "△")  ("●", "○")
#
# ------------------------------------------------------------
# 🗣️ Emoji für Meldungen / Events
# ------------------------------------------------------------
# Eingabe / Hinweis:     ⌨️ 📝 👉 ℹ️
# Erfolg / Paar:         🎯 ✅ ✔️ ✨ 🔥 🧠 🎉
# Misserfolg / kein Paar:💩 🙈 🤡 💥 🫠
# Fehler / Warnung:      ⚠️ ❌ 🚫 🚧 ❓
# Ungültige Koordinaten: 🧭 🗺️ 🚧 ❓
# Schon aufgedeckt:      👀 🔁 🙃
# Gleiche Karte gewählt: 🪞 ♻️ 😄
# Abbruch / Quit:        🛑 🚪 👋
# Spielende / Sieg:      🏆 🥇 🏁 🎊
# Undo / History (Bonus):↩️ 🕘 📜
#
# ------------------------------------------------------------
# 💬 Beispiel-Meldungen (fertige Textbausteine)
# ------------------------------------------------------------
# "⚠️ Bitte zwei Koordinaten eingeben (z. B. A0 D1)."
# "🚧 Ungültige Koordinaten."
# "🪞 Zwei verschiedene Karten, bitte."
# "👀 Die Karte ist schon aufgedeckt."
# "🎯 Paar gefunden!"
# "💩 Kein Paar."
# "🏆 Glückwunsch! Alle Paare gefunden!"
# "🛑 Spiel beendet."
# ------------------------------------------------------------


import random
import string
import time
import math
import os



class SpielAbbruch(Exception):
    pass



class GridView:

    def __init__(self, anzahl_paare: int, anzahl_spalten: int) -> None:
        assert isinstance(anzahl_paare, int) and anzahl_paare > 0, "Anzahl Paare muss positver int sein"
        assert isinstance(anzahl_spalten, int) and anzahl_spalten > 0, "Anzahl Spalten muss positver int sein"
        assert anzahl_spalten <= 26, "Maximal 26 Spalten (A-Z) unterstützt."


        self.anzahl_karten: int = anzahl_paare*2
        self.anzahl_zeilen: int = (self.anzahl_karten + anzahl_spalten - 1)  // anzahl_spalten
        self.anzahl_spalten: int = anzahl_spalten

        zeilen_header_raw: list[str] = [str(y) for y in range(self.anzahl_zeilen)]
        self.zeilen_header: list[str] = [s.rjust(2) for s in zeilen_header_raw]

        spalten_header_raw: list[str] = list(string.ascii_uppercase[:anzahl_spalten])
        self.spalten_header: list[str] = [s.rjust(2) for s in spalten_header_raw]

        coords: list[str] = [
            x + y
            for y in zeilen_header_raw
            for x in spalten_header_raw
        ]

        self.position: dict[str, int] = {
            pos: idx
            for idx, pos in enumerate(coords[:self.anzahl_karten])
        }
    
    
    def get_index(self, pos: str) -> int | None:
        return self.position.get(pos)
    


    def render_karten(self, karten: list[str]) -> str:
        assert len(karten) == self.anzahl_karten

        os.system("cls" if os.name == "nt" else "clear")

        lines: list[str] = [" ".rjust(2), *self.zeilen_header]

        lines = [y + " " for y in lines]

        lines[0] += " ".join(self.spalten_header)
        
        for j in range(self.anzahl_zeilen):
            lines[j+1] += " ".join(karten[j*self.anzahl_spalten:(j+1)*self.anzahl_spalten])

        return "\n".join(lines)



class Karte:

    def __init__(self, symbol: str, farbe: str) -> None:
        self.symbol: str = symbol      # Vorderseite
        self.farbe: str  = farbe       # Rückseite
        self._aufgedeckt = False

    def aufdecken(self) -> None:
        self._aufgedeckt = True

    def aufgedeckt(self) -> bool:
        return self._aufgedeckt

    def zudecken(self) -> None:
        self._aufgedeckt = False

    def vergleichen(self, andere: "Karte") -> bool:
        return self.symbol == andere.symbol

    def sichtbar(self) -> str:
        if self._aufgedeckt:
            return self.symbol
        return self.farbe

class History:
    def __init__(self):
        self.history = []

    def push(self, zug):
        self.history.append(zug)

    def pop(self):
        if len(self.history) > 0:
            return self.history.pop()
        return None

class Spieler:
    def __init__(self, name: str):
        self.name = name
        self.punkte = 0

    def punkte_erhoehen(self):
        self.punkte += 1

    def __str__(self):
        return f"{self.name} ({self.punkte} Punkte)"


class Memory:

    grid_view: GridView
    history: History

    def __init__(self, karte_vorne: tuple[str, ...], karte_hinten: tuple[str, str]) -> None:
        assert len(karte_vorne) > 0,   "Mindestens ein Paar nötig."
        assert len(karte_hinten) == 2, "Es müssen genau zwei Rückseiten sein."
        
        self.stapel: list[Karte] = []
        for hinten in karte_hinten:
            for vorne in karte_vorne:
                self.stapel.append(Karte(vorne, hinten))

        random.shuffle(self.stapel)

        anzahl_paare: int = len(karte_vorne)     
        self.grid_view = GridView(anzahl_paare, math.ceil(math.sqrt(anzahl_paare*2)))
        self.history = History()
        self.spieler1 = Spieler("Spieler 1")
        self.spieler2 = Spieler("Spieler 2")
        self.zug_anzahl = 0

    def spielfeld(self) -> None:
        karten: list[str] = [k.sichtbar() for k in self.stapel]
        print(self.grid_view.render_karten(karten))
    
    def undo(self):
        last_move = self.history.pop()
        if last_move is None:
            print("Kein Zug zum Rückgängig machen.")
            return

        i, j, war_paar = last_move

        self.stapel[i].zudecken()
        self.stapel[j].zudecken()

        self.zug_anzahl -= 1

        if war_paar:
            if self.zug_anzahl % 2 == 0:
                self.spieler1.punkte -= 1
            else:
                self.spieler2.punkte -= 1

        print("↩️ Zug rückgängig gemacht.")


    def frage_zug(self) -> tuple[int, int]:

        while True:
            self.spielfeld()

            if self.zug_anzahl % 2 == 0:
                print(f"{self.spieler1.name} ist an der Reihe")
                spieler = self.spieler1
            else:
                print(f"{self.spieler2.name} ist an der Reihe")
                spieler = self.spieler2


            try:
                raw = input("Zwei Karten (z. B. A0 D1) oder 'quit' zum Beenden oder 'undo' um den letzten Zug rückgängig zu machen: ").strip()
            except KeyboardInterrupt:
                print()
                raise SpielAbbruch()
            
            if raw.lower() == "quit":
                raise SpielAbbruch()
            elif raw.lower() == "undo":
                self.undo()
                continue


            try:
                x, y = raw.split()
            except ValueError:
                print("⚠️ Bitte zwei Koordinaten eingeben (z. B. A0 D1).")
                time.sleep(1.5)
                continue

            i: int | None = self.grid_view.get_index(x.upper())
            j: int | None = self.grid_view.get_index(y.upper())

            if i is None or j is None:
                print("🚧 Ungültige Koordinaten.")
                time.sleep(1.5)
                continue

            if i == j:
                print("🪞 Zwei verschiedene Karten, bitte.")
                time.sleep(1.5)
                continue

            if self.stapel[i].aufgedeckt() == True or self.stapel[j].aufgedeckt() == True:
                print("👀 Die Karte ist schon aufgedeckt.")
                time.sleep(1.5)
                continue

            return i, j



    def spielen(self) -> None:
        try:
            while any(k.aufgedeckt() == False for k in self.stapel):
                i, j = self.frage_zug()

                self.stapel[i].aufdecken()
                self.stapel[j].aufdecken()
                self.spielfeld()

                if self.stapel[i].vergleichen(self.stapel[j]):
                    print("🎯 Paar gefunden!")
                    if self.zug_anzahl % 2 == 0:
                        self.spieler1.punkte_erhoehen()
                    else:
                        self.spieler2.punkte_erhoehen()


                else:
                    print("💩 Kein Paar.")
                    time.sleep(2)
                    self.stapel[i].zudecken()
                    self.stapel[j].zudecken()

                time.sleep(1.5)
                self.zug_anzahl += 1
                self.history.push((i, j))

                self.history.push((i, j, self.stapel[i].vergleichen(self.stapel[j])))



            print(f"🏆 Glückwunsch! Alle Paare gefunden! Benötigete Züge: {self.zug_anzahl}")
            if self.spieler1.punkte > self.spieler2.punkte:
                print(f"{self.spieler1.name} hat gewonnen mit {self.spieler1.punkte} Punkten!")
            elif self.spieler1.punkte < self.spieler2.punkte:
                 print(f"{self.spieler2.name} hat gewonnen mit {self.spieler2.punkte} Punkten!")
            else:
                print("Unentschieden!")

        except SpielAbbruch:
            print("🛑 Spiel beendet.")
        



mem1 = Memory(("🐍", "🐢", "🐸"), ("🟦", "🟥"))
mem1.spielen()





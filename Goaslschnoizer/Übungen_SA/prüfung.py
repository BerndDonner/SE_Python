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
from messages import MSG
from values import WERTE


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

        self._history: list[dict] = []

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
    
    def get_pos(self, idx: int) -> str:
    
        zeile = idx // self.anzahl_spalten
        spalte = idx % self.anzahl_spalten
        return string.ascii_uppercase[spalte] + str(zeile)



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
    
    def __init__(self) -> None:
        self._zuege: list[dict] = []
    
    def hinzufügen(self, turn_no: int, i: int, j: int, match: bool) -> None:

        zug = { "turn_no": turn_no, "i": i, "j": j, "match": match }
        
        self._zuege.append(zug)

    def anzeigen(self, grid_view: GridView) -> None:
        if not self._zuege:
            print("\n📜 Noch keine Züge gemacht.")
            return
    
        print("\n📜 Letzte Züge:")
        for zug in self._zuege[-5:]:
            pos1 = grid_view.get_pos(zug["i"])
            pos2 = grid_view.get_pos(zug["j"])
            result = "OK" if zug["match"] else "MISS"
            print(f"#{zug['turn_no']} {pos1} {pos2} -> {result}")
        print()
    

class Memory:

    grid_view: GridView

    def __init__(self, karte_vorne: tuple[str, ...], karte_hinten: tuple[str, str]) -> None:
        assert len(karte_vorne) > 0,   "Mindestens ein Paar nötig."
        assert len(karte_hinten) == 2, "Es müssen genau zwei Rückseiten sein."

        self.rng = random.Random(12345)

        self._score: int = 0
        self._zuege: int = 0
        self._treffer: int = 0

        self.history = History()
        
        self.stapel: list[Karte] = []
        for hinten in karte_hinten:
            for vorne in karte_vorne:
                self.stapel.append(Karte(vorne, hinten))

        random.shuffle(self.stapel)

        anzahl_paare: int = len(karte_vorne)     
        self.grid_view = GridView(anzahl_paare, math.ceil(math.sqrt(anzahl_paare*2)))


    def spielfeld(self) -> None:
        karten: list[str] = [k.sichtbar() for k in self.stapel]
        print(self.grid_view.render_karten(karten))
    
    def msg(self, key: str) -> str:
        assert key in MSG, f"Unbekannter Key: {key}"
        return self.rng.choice(MSG[key])
    
    def zeige_statistik(self) -> None:
        
        print(f"Züge:        {self._zuege}")
        print(f"Treffer:     {self._treffer}")
    
   
        if self._zuege > 0:
            trefferquote = round((self._treffer / self._zuege) * 100)
        else:
            trefferquote = 0
    
        print(f"Trefferquote: {trefferquote}%")
        print(f"Score:       {self._score}")
        


    def frage_zug(self) -> tuple[int, int]:
        while True:
            self.spielfeld()

            try:
                raw = input(self.msg("prompt")).strip()
            except KeyboardInterrupt:
                print()
                raise SpielAbbruch()
            
            if raw.lower() == "history":
                self.history.anzeigen(self.grid_view)
                input("\nDrücke Enter zum Weiterspielen...")
                continue

            try:
                x, y = raw.split()
            except ValueError:
                print(self.msg("need_two"))
                time.sleep(1.5)
                continue

            i: int | None = self.grid_view.get_index(x.upper())
            j: int | None = self.grid_view.get_index(y.upper())

            if i is None or j is None:
                print(self.msg("invalid"))
                time.sleep(1.5)
                continue

            if i == j:
                print(self.msg("same_card"))
                time.sleep(1.5)
                continue

            if self.stapel[i].aufgedeckt() == True or self.stapel[j].aufgedeckt() == True:
                print(self.msg("already_open"))
                time.sleep(1.5)
                continue

            return i, j



    def spielen(self) -> None:
        try:
            while any(k.aufgedeckt() == False for k in self.stapel):
                i, j = self.frage_zug()

                self._zuege += 1

                self.stapel[i].aufdecken()
                self.stapel[j].aufdecken()
                self.spielfeld()

                if self.stapel[i].vergleichen(self.stapel[j]):
                    self._treffer += 1
                    kartenwert = WERTE[self.stapel[i].symbol]
                    self._score += kartenwert

                    self.history.hinzufügen(self._zuege, i, j, match=True)

                    print(self.msg("match"))

                else:
                    self._score -= 1
                    print(self.msg("miss"))
                    self.stapel[i].zudecken()
                    self.stapel[j].zudecken()

                    self.history.hinzufügen(self._zuege, i, j, match=False)

                time.sleep(1.5)

            print(self.msg("win"))

            self.zeige_statistik()

            self.history.anzeigen(self.grid_view)

            

        except SpielAbbruch:
            print(self.msg("quit"))


mem1 = Memory(("🐍", "🐢", "🐸"), ("🟦", "🟥"))
mem1.spielen()


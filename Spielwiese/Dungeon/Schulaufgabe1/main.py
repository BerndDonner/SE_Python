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
from dataclasses import dataclass
from messages import MSG



class SpielAbbruch(Exception):
    pass

@dataclass(frozen=True, slots=True)
class Zug:
    turn_no: int
    idx1: int
    idx2: int
    result: bool


class History:

    zuege: list[Zug]

    def __init__(self) -> None:
        self.zuege = []

    def push(self, zug: Zug) -> None:
        self.zuege.append(zug)

    def pop(self) -> Zug | None:
        if len(self.zuege) == 0:
            return None
        return self.zuege.pop()

    def get_zuege(self, num_zuege: int) -> list[Zug]:
        assert num_zuege >= 0
        num_zuege = min(num_zuege, len(self.zuege))

        return self.zuege[-num_zuege:] 


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

        self.index: list[str] = coords[:self.anzahl_karten]
        
        self.position: dict[str, int] = {
            pos: idx
            for idx, pos in enumerate(self.index)
        }
    
    def get_index(self, pos: str) -> int | None:
        return self.position.get(pos)

    def get_pos(self, idx: int) -> str:
        assert idx < self.anzahl_karten
        return self.index[idx]

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

    def __init__(self, symbol: str, farbe: str, wert: int) -> None:
        self.symbol: str = symbol      # Vorderseite
        self.farbe: str  = farbe       # Rückseite
        self._wert: int   = wert
        self._aufgedeckt = False

    def aufdecken(self) -> None:
        self._aufgedeckt = True

    def aufgedeckt(self) -> bool:
        return self._aufgedeckt

    def zudecken(self) -> None:
        self._aufgedeckt = False

    def wert(self) -> int:
        return self._wert

    def vergleichen(self, andere: "Karte") -> bool:
        return self.symbol == andere.symbol

    def sichtbar(self) -> str:
        if self._aufgedeckt:
            return self.symbol
        return self.farbe


class Memory:

    grid_view: GridView
    history: History
    
    def __init__(self, karte_vorne: tuple[tuple[str, int], ...], karte_hinten: tuple[str, str]) -> None:
        assert len(karte_vorne) > 0,   "Mindestens ein Paar nötig."
        assert len(karte_hinten) == 2, "Es müssen genau zwei Rückseiten sein."
        
        self.rng: random.Random = random.Random(12345)

        self.stapel: list[Karte] = []
        for hinten in karte_hinten:
            for vorne in karte_vorne:
                self.stapel.append(Karte(vorne[0], hinten, vorne[1]))

        self.rng.shuffle(self.stapel)

        anzahl_paare: int = len(karte_vorne)
        self.grid_view = GridView(anzahl_paare, math.ceil(math.sqrt(anzahl_paare*2)))
        self.score: int = 0
        self.zuege: int = 0
        self.treffer: int = 0
        self.history = History()

    def msg(self, key: str) -> str:
        assert key in MSG
        return self.rng.choice(MSG[key])

    def spielfeld(self) -> None:
        karten: list[str] = [k.sichtbar() for k in self.stapel]
        print(self.grid_view.render_karten(karten))


    def frage_zug(self) -> tuple[int, int]:
        while True:
            self.spielfeld()

            try:
                raw: str = input(self.msg("prompt")).strip()
            except KeyboardInterrupt:
                print()
                raise SpielAbbruch()

            if raw.lower() == "history":
                for z in self.history.get_zuege(5):
                    pos1: str = self.grid_view.get_pos(z.idx1)
                    pos2: str = self.grid_view.get_pos(z.idx2)
                    result: str = "MATCH" if z.result else "MISS"
                                        
                    print("#" + str(z.turn_no) + " " + pos1 + " " + pos2 + " -> " + result)
                time.sleep(3)
                continue

            if raw.lower() == "undo":
                zug: Zug | None = self.history.pop()
                if zug == None: continue
                self.zuege -= 1
                if zug.result:
                    i: int = zug.idx1
                    j: int = zug.idx2
                    assert self.stapel[i].wert() == self.stapel[j].wert(), "Nicht identische Karten in History als Treffer gespeichert"
                    self.stapel[i].zudecken()
                    self.stapel[j].zudecken()
                    self.treffer -= 1
                    self.score -= self.stapel[i].wert()

                else:
                    self.score += 1
                                
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
                self.zuege += 1

                self.stapel[i].aufdecken()
                self.stapel[j].aufdecken()
                self.spielfeld()

                if self.stapel[i].vergleichen(self.stapel[j]):
                    self.treffer += 1
                    self.score += self.stapel[i].wert()
                    print(self.msg("match"))
                    self.history.push(Zug(turn_no=self.zuege, idx1=i, idx2=j, result=True))
                else:
                    print(self.msg("miss"))
                    self.history.push(Zug(turn_no=self.zuege, idx1=i, idx2=j, result=False))
                    self.score -= 1
                    self.stapel[i].zudecken()
                    self.stapel[j].zudecken()

                time.sleep(1.5)

            print(self.msg("win"))
            quote: int = round(self.treffer * 100 / self.zuege) if self.zuege > 0 else 0
            print(f"📊 Statistik: Züge={self.zuege}, Treffer={self.treffer}, Quote={quote}%, Score={self.score}")
        except SpielAbbruch:
            print(self.msg("quit"))



mem1 = Memory((("🐍", 1) , ("🐢", 2), ("🐸", 3)), ("🟦", "🟥"))
mem1.spielen()

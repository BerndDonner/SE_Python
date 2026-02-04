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

MSG: dict[str, list[str]] = {
    "match": [
        "🎯 Paar gefunden!",
        "✅ Treffer!",
        "✨ Sauber!",
        "🧠 Stark gemerkt!",
        "🔥 Läuft!",
        "🎉 Nice!",
        "✔️ Volltreffer!",
        "🏆 Das zählt!",
    ],
    "miss": [
        "💩 Kein Paar.",
        "🙈 Daneben.",
        "🤡 Nope.",
        "💥 Knapp vorbei!",
        "🫠 Leider nicht.",
        "❌ Kein Match.",
        "😄 Nächster Versuch!",
        "🔁 Noch mal!",
    ],
    "need_two": [
        "⚠️ Bitte zwei Koordinaten eingeben (z. B. A0 D1).",
        "📝 Genau zwei Koordinaten, bitte (A0 D1).",
        "⌨️ Zwei Felder eingeben, z. B. A0 D1.",
    ],
    "invalid": [
        "🚧 Ungültige Koordinaten.",
        "❌ Das gibt’s nicht.",
        "🧭 Falsches Feld.",
        "🗺️ Diese Position existiert nicht.",
        "⚠️ Bitte gültige Koordinaten eingeben.",
        "🚫 Außerhalb des Spielfelds.",
        "❓ Was war das denn?",
        "📝 Beispiel: A0 D1",
    ],
    "already_open": [
        "👀 Die Karte ist schon aufgedeckt.",
        "🔁 Dieses Feld ist bereits offen.",
        "🙃 Schon sichtbar!",
        "🚫 Nimm zwei verdeckte Karten.",
        "⚠️ Eine der Karten ist schon offen.",
        "👀 Bitte andere Karten wählen.",
        "🔁 Das zählt nicht, schon aufgedeckt.",
        "😄 Such dir zwei neue.",
    ],
    "same_card": [
        "🪞 Zwei verschiedene Karten, bitte.",
        "♻️ Nicht zweimal dieselbe Karte!",
        "😄 Das ist nur eine Karte.",
        "🚫 Du musst zwei verschiedene wählen.",
        "🪞 Ein Feld reicht nicht.",
        "⚠️ Unterschiedliche Koordinaten eingeben.",
        "♻️ Gleiche Karte doppelt geht nicht.",
        "👉 Wähle zwei verschiedene Felder.",
    ],
    "prompt": [
        "⌨️ Zwei Karten (z. B. A0 D1) oder Ctrl-C zum Beenden: ",
        "📝 Eingabe: zwei Koordinaten (A0 D1) oder Ctrl-C: ",
        "👉 Deine Wahl (A0 D1) – Ctrl-C beendet: ",
        "⌨️ Zug eingeben (z. B. A0 D1): ",
        "🧩 Welche zwei Karten? (A0 D1) ",
        "📜 Zwei Koordinaten bitte (A0 D1): ",
    ],
    "quit": [
        "🛑 Spiel beendet.",
        "👋 Bis zum nächsten Mal!",
        "🚪 Abbruch – Spiel Ende.",
        "🛑 Okay, beendet.",
        "👋 Tschüss!",
        "🚪 Alles klar, wir stoppen hier.",
    ],
    "win": [
        "🏆 Glückwunsch! Alle Paare gefunden!",
        "🥇 Gewonnen! Alles aufgedeckt!",
        "🏁 Fertig! Du hast alle Paare!",
        "🎊 Sieg! Starke Leistung!",
        "🏆 Durchgespielt – alle Paare!",
        "🎉 Alles gefunden! Top!",
    ],
}

WERTE: dict[str, int] = {
    # Tiere
    "🐍": 1, "🐢": 2, "🐸": 3, "🦊": 2, "🐙": 4, "🦄": 5,
    "🦖": 4, "🐝": 1, "🦉": 3, "🐧": 2, "🦁": 4, "🐳": 5,

    # Essen
    "🍕": 2, "🍔": 2, "🍟": 1, "🍣": 4, "🍩": 2, "🍪": 1,
    "🍎": 1, "🍉": 2, "🍓": 2, "🍌": 1, "🍇": 2, "🥨": 1,

    # Technik
    "💾": 3, "💿": 2, "📟": 3, "📺": 2, "🖥️": 4, "⌨️": 3,
    "🖱️": 2, "🔌": 2, "🔋": 2, "📡": 4, "🛰️": 5, "🧲": 3,

    # Dinge
    "🎲": 2, "🎯": 3, "🧩": 3, "🧠": 4, "🧪": 3, "🧯": 2,
    "🔧": 2, "🪛": 2, "🧱": 2, "🧭": 3, "🔑": 3, "🏆": 5,
}



from pickle import FALSE, TRUE
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
      
        self.cords: list[str]= coords
    
    
    def get_index(self, pos: str) -> int | None:
        return self.position.get(pos)
    
    def get_pos(self, idx:int) -> str | None:
        return self.cords[idx]



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


class Memory:

    grid_view: GridView

    def __init__(self, karte_vorne: tuple[str, ...], karte_hinten: tuple[str, str]) -> None:
        assert len(karte_vorne) > 0,   "Mindestens ein Paar nötig."
        assert len(karte_hinten) == 2, "Es müssen genau zwei Rückseiten sein."
        self.rng = random.Random(12345)
        self.stapel: list[Karte] = []
        for hinten in karte_hinten:
            for vorne in karte_vorne:
                self.stapel.append(Karte(vorne, hinten))

        random.shuffle(self.stapel)
        self._match: bool= False
        anzahl_paare: int = len(karte_vorne)     
        self.grid_view = GridView(anzahl_paare, math.ceil(math.sqrt(anzahl_paare*2)))
        self._score: int = 0
        self._zuege: int = 0
        self._treffer: int = 0
        self._history: list[dict] =[]


    def message(self, key: str) -> str:
       assert key in MSG, f"Unbekannter MSG-Key: {key}"
       return self.rng.choice(MSG[key])
       
    def spielfeld(self) -> None:
        karten: list[str] = [k.sichtbar() for k in self.stapel]
        print(self.grid_view.render_karten(karten))

    def zeige_history(self) -> None:
        self.spielfeld()
        if len(self._history) == 0:
            print("Noch keine Züge vorhanden.")
        else:
            print("Letzte Züge:")
            #kords: list[str]=self.grid_view.cords
            for x in self._history[-5:]:
                turn_no = x["turn_no"]
                i = x["i"]
                j = x["j"]
                match = x["match"]
            
                if match == True: y = "OK" 
                else: y ="MISS"
                z = self.grid_view.get_pos(i)
                w=self.grid_view.get_pos(j)

                print(f"#{turn_no} {z} {w} -> {y}")

        
        time.sleep(5)
        

    def frage_zug(self) -> tuple[int, int]:
        while True:
            self.spielfeld()
            
            try:
                raw = input(f"ctrl+c für spielende and history für letzten 5 züge\n{self.message("prompt")} ").strip()
            except KeyboardInterrupt:
                print()
                raise SpielAbbruch()
            
            if raw.lower() == "history":
                self.zeige_history()
                continue


            try:
                x, y = raw.split()
            except ValueError:
                print(self.message("need_two"))
                time.sleep(1.5)
                continue

            

            i: int | None = self.grid_view.get_index(x.upper())
            j: int | None = self.grid_view.get_index(y.upper())

            if i is None or j is None:
                print(self.message("invalid"))
                time.sleep(1.5)
                continue

            if i == j:
                print(self.message("same_card"))
                time.sleep(1.5)
                continue

            if self.stapel[i].aufgedeckt() == True or self.stapel[j].aufgedeckt() == True:
                print(self.message("already_open"))
                time.sleep(1.5)
                continue
            self._zuege += 1
            return i, j



    def spielen(self) -> None:
        try:
            while any(k.aufgedeckt() == False for k in self.stapel):
                i, j = self.frage_zug()

                self.stapel[i].aufdecken()
                self.stapel[j].aufdecken()
                self.spielfeld()

                if self.stapel[i].vergleichen(self.stapel[j]):
                    print(self.message("match"))
                    self._score  += int(WERTE.get(str(self.stapel[i]),1))
                    self._treffer += 1
                    self._match = True
                else:
                    print(self.message("miss"))
                    self.stapel[i].zudecken()
                    self.stapel[j].zudecken()
                    self._score -= 1
                    self._match = False

                self._history.append({
                    "turn_no": self._zuege,
                    "i": i,
                    "j": j,
                    "match": self._match
                })    
                time.sleep(1.5)

            print(self.message("win"))
            print(f'Zuege: {self._zuege}')
            print(f'Treffer: {self._treffer} ')
            prozent: float= (self._treffer / self._zuege)*100 
            print(f'Trefferquote: {prozent}%')
            print(f'Score: {self._score} ')

        except SpielAbbruch:
            print(self.message("quit"))




mem1 = Memory(("🐍", "🐢", "🐸"), ("🟦", "🟥"))
mem1.spielen()


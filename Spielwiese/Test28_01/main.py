import random
import string
import time
import math
import os


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
        if self._aufgedeckt: return self.symbol
        return self.farbe


class Memory:

    grid_view: GridView

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


    def spielfeld(self) -> None:
        karten: list[str] = [k.sichtbar() for k in self.stapel]
        print(self.grid_view.render_karten(karten))

    def spielen(self) -> None:
        while any(k.aufgedeckt() == False for k in self.stapel):
            self.spielfeld()
            try:
                x, y = input("Welche zwei Karten möchten Sie aufdecken (z. B. A0 D1)? ").split()
            except ValueError as e:
                print("Bitte zwei Zahlen eingeben.", e)
                time.sleep(1.5)
                continue

            
            i: int | None = self.grid_view.get_index(x.upper())
            if i is None:
                print("Ungültige Koordinaten.")
                time.sleep(1.5)
                continue
            
            j: int | None = self.grid_view.get_index(y.upper())
            if j is None:
                print("Ungültige Koordinaten.")
                time.sleep(1.5)
                continue

            if self.stapel[i].aufgedeckt() == True or self.stapel[j].aufgedeckt() == True:
                print("Diese Karte ist schon aufgedeckt.")
                time.sleep(1.5)
                continue

            self.stapel[i].aufdecken()
            self.stapel[j].aufdecken()

            self.spielfeld()


            if self.stapel[i].vergleichen(self.stapel[j]):
                print("Paar gefunden!")

            else:
                print("Kein Paar.")
                self.stapel[i].zudecken()
                self.stapel[j].zudecken()
            time.sleep(1.5)

        print("Glückwunsch! Du hast alle Paare gefunden.")

m1 = Memory(("🐍", "🐢", "🐸"), ("🟦", "🟥"))
m1.spielen()


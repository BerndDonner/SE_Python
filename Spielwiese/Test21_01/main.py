import random
import time
import os


class Karte:
    def __init__(self, symbol: str, farbe: str):
        self.symbol = symbol
        self.farbe = farbe
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
        return self.symbol if self._aufgedeckt else self.farbe


class Grid:
    """Grid mit Koordinaten (A1, B2, ...) und Rendering."""
    def __init__(self, anzahl_karten: int, spalten: int):
        if anzahl_karten <= 0:
            raise ValueError("anzahl_karten muss > 0 sein.")
        if spalten <= 0:
            raise ValueError("spalten muss > 0 sein.")
        if spalten > 26:
            raise ValueError("Maximal 26 Spalten (A-Z) unterstützt.")

        self.anzahl_karten = anzahl_karten
        self.spalten = spalten
        self.zeilen = (anzahl_karten + spalten - 1) // spalten

        # Mapping aufbauen
        self.coord2idx: dict[str, int] = {}
        self.idx2coord: list[str] = []

        for idx in range(self.anzahl_karten):
            col = idx % self.spalten
            row = idx // self.spalten
            coord = f"{chr(ord('A') + col)}{row + 1}"
            self.coord2idx[coord] = idx
            self.idx2coord.append(coord)

    def koordinate_zu_index(self, s: str) -> int:
        s = s.strip().upper()
        if s not in self.coord2idx:
            max_col = chr(ord("A") + self.spalten - 1)
            raise ValueError(f"Ungültige Koordinate. Erlaubt: A1 bis {max_col}{self.zeilen}.")
        return self.coord2idx[s]

    def index_zu_koordinate(self, idx: int) -> str:
        if idx < 0 or idx >= self.anzahl_karten:
            raise ValueError("Index außerhalb des Bereichs.")
        return self.idx2coord[idx]

    def _indices_zeile(self, r: int) -> list[int | None]:
        start = r * self.spalten
        out: list[int | None] = []
        for c in range(self.spalten):
            idx = start + c
            out.append(idx if idx < self.anzahl_karten else None)
        return out

    def render(self, zellen: list[str]) -> str:
        if len(zellen) != self.anzahl_karten:
            raise ValueError("zellen muss genau anzahl_karten Elemente enthalten.")

        lines: list[str] = []
        head = "     " + "".join(f" {chr(ord('A') + c):2} " for c in range(self.spalten))
        lines.append(head)

        for r in range(self.zeilen):
            row = f"{r + 1:>3} "
            for idx in self._indices_zeile(r):
                if idx is None:
                    row += "   "
                else:
                    row += f" {zellen[idx]} "
            lines.append(row)

        return "\n".join(lines)


class Memory:
    def __init__(self, karte_vorne: tuple[str, ...], karte_hinten: tuple[str, str], spalten: int):
        if len(karte_hinten) != 2:
            raise ValueError("karte_hinten muss genau 2 Rückseiten enthalten.")

        self.kombis: list[Karte] = []
        for hinten in karte_hinten:
            for vorne in karte_vorne:
                self.kombis.append(Karte(vorne, hinten))

        random.shuffle(self.kombis)
        self.grid = Grid(len(self.kombis), spalten)

    def _clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def spielfeld(self) -> None:
        self._clear()
        sicht = [k.sichtbar() for k in self.kombis]
        print(self.grid.render(sicht))
        print()

    def spielen(self) -> None:
        while any(not k.aufgedeckt() for k in self.kombis):
            self.spielfeld()

            try:
                s1, s2 = input("Zwei Karten (z. B. A1 B2): ").split()
                i = self.grid.koordinate_zu_index(s1)
                j = self.grid.koordinate_zu_index(s2)
            except ValueError as e:
                print("Ungültige Eingabe:", e)
                time.sleep(1.5)
                continue

            if i == j:
                print("Bitte zwei verschiedene Karten wählen.")
                time.sleep(1.5)
                continue

            if self.kombis[i].aufgedeckt() or self.kombis[j].aufgedeckt():
                print("Mindestens eine Karte ist schon aufgedeckt.")
                time.sleep(1.5)
                continue

            self.kombis[i].aufdecken()
            self.kombis[j].aufdecken()
            self.spielfeld()

            if self.kombis[i].vergleichen(self.kombis[j]):
                print("Paar gefunden!")
            else:
                print("Kein Paar.")
                time.sleep(1.0)
                self.kombis[i].zudecken()
                self.kombis[j].zudecken()

            time.sleep(1.0)

        self.spielfeld()
        print("Glückwunsch! Du hast alle Paare gefunden.")


m1 = Memory(("🐍", "🐢", "🐸"), ("🟦", "🟥"), spalten=4)
m1.spielen()

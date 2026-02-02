class Gitter:
    def __init__(self, spalten: int, zeilen: int, anzahl_sachen: int, platzhalter: str = "."):
        import string

        assert 1 <= spalten <= 26, "Spalten: 1–26 erlaubt"
        assert zeilen > 0, "Zeilen müssen > 0 sein"
        assert 0 <= anzahl_sachen <= spalten * zeilen, "Zu viele Sachen für das Gitter"

        self.spalten = spalten
        self.zeilen = zeilen
        self.anzahl_sachen = anzahl_sachen
        self.platzhalter = platzhalter
        self.gesamt_felder = spalten * zeilen
        self.daten = [platzhalter] * self.gesamt_felder
        self.spalten_beschriftung = string.ascii_uppercase[:spalten]

    # ---------- Position zu Index ----------
    def pos_zu_index(self, pos: str) -> int:
        """
        Wandelt 'A0', 'B1' etc. in den 1D-Index der Liste um
        """
        pos = pos.strip().upper()
        if len(pos) < 2:
            raise ValueError("Ungültige Position")

        spalte_buchstabe = pos[0]
        zeile = pos[1:]

        if not zeile.isdigit():
            raise ValueError("Zeilenangabe muss eine Zahl sein")

        x = ord(spalte_buchstabe) - ord("A")  # 'A'->0, 'B'->1, ...
        y = int(zeile)

        index = y * self.spalten + x
        if index >= self.gesamt_felder:
            raise IndexError("Position außerhalb des Gitters")
        return index

    # ---------- Item einsetzen ----------
    def einsetzen(self, pos: str, wert: str):
        idx = self.pos_zu_index(pos)
        self.daten[idx] = wert

    # ---------- Anzeige ----------
    def anzeigen(self):
        import os
        os.system("cls" if os.name == "nt" else "clear")

        # Spaltenüberschrift
        print("   " + " ".join(self.spalten_beschriftung))

        # Jede Zeile
        for zeilen_index in range(self.zeilen):
            zeile = []
            for spalten_index in range(self.spalten):
                index = zeilen_index * self.spalten + spalten_index
                zeile.append(self.daten[index] if index < self.anzahl_sachen else " ")
            print(f"{zeilen_index:2} " + " ".join(zeile))

        print("\nLegende: '.' = Platzhalter, leer = freies Feld")

grid = Gitter(spalten=3, zeilen=3, anzahl_sachen=8)
grid.einsetzen("A0", "A")
grid.einsetzen("B0", "B")
grid.einsetzen("C0", "C")
grid.einsetzen("A1", "D")
grid.einsetzen("B1", "E")
grid.einsetzen("C1", "F")
grid.einsetzen("A2", "G")
grid.einsetzen("B2", "H")

grid.anzeigen()        
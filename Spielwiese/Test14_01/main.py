import random


class Card:
    def __init__(self, vorne: str, hinten: str):
        self.vorne = vorne
        self.hinten = hinten
        self.sichtbar = "hinten"  # "hinten" oder "vorne"

    def zeige_symbol(self) -> str:
        return self.vorne if self.sichtbar == "vorne" else self.hinten

    def ist_vorne(self) -> bool:
        return self.sichtbar == "vorne"

    def aufdecken(self) -> None:
        self.sichtbar = "vorne"

    def zudecken(self) -> None:
        self.sichtbar = "hinten"


class MemoryGame:
    def __init__(self, karte_vorne: tuple[str, ...], karte_hinten: tuple[str, ...]):
        # Alle Karten bauen (wie vorher), aber als Objekte
        self.karten: list[Card] = []
        for hinten in karte_hinten:
            for vorne in karte_vorne:
                self.karten.append(Card(vorne=vorne, hinten=hinten))

        random.shuffle(self.karten)

    def spielfeld(self) -> None:
        # Anzeige ist jetzt eine Methode und nutzt self.karten
        symbole = [k.zeige_symbol() for k in self.karten]
        print("Karten: ", *symbole)
        print("Index:  ", end=" ")
        for i in range(len(symbole)):
            print(f"{i:2}", end=" ")
        print("\n")

    def ist_fertig(self) -> bool:
        # Fertig, wenn alle Karten vorne sind
        return all(k.ist_vorne() for k in self.karten)

    def _indizes_gueltig(self, i: int, j: int) -> bool:
        # Kleine Schutzfunktion gegen Abstürze bei falscher Eingabe
        if i == j:
            return False
        if i < 0 or i >= len(self.karten):
            return False
        if j < 0 or j >= len(self.karten):
            return False
        return True

    def zug(self, i: int, j: int) -> None:
        # Ein kompletter Zug: prüfen, aufdecken, vergleichen, ggf. zudecken
        if not self._indizes_gueltig(i, j):
            print("Ungültige Indizes.")
            return

        if self.karten[i].ist_vorne() or self.karten[j].ist_vorne():
            print("Diese Karte ist schon aufgedeckt.")
            return

        self.karten[i].aufdecken()
        self.karten[j].aufdecken()

        self.spielfeld()

        if self.karten[i].vorne == self.karten[j].vorne:
            print("Paar gefunden!")
        else:
            print("Kein Paar.")
            self.karten[i].zudecken()
            self.karten[j].zudecken()

    def play(self) -> None:
        # Hauptspiel-Schleife (war vorher der while-Block)
        while not self.ist_fertig():
            self.spielfeld()

            try:
                i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
            except ValueError as e:
                print("Bitte zwei Zahlen eingeben.", e)
                continue

            self.zug(i, j)

        print("Glückwunsch! Du hast alle Paare gefunden.")


# --- Start ---
karte_vorne = ("🐍", "🐢", "🐸")
karte_hinten = ("🟦", "🟥")

spiel = MemoryGame(karte_vorne=karte_vorne, karte_hinten=karte_hinten)
spiel.play()

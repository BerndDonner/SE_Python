import random
import time
import os

class XXX:

    def __init__(self, anzahl_paare: int, anzahl_spalten: int):
        assert isinstance(anzahl_paare, int) and anzahl_paare > 0
        assert isinstance(anzahl_spalten, int) and anzahl_spalten > 0

        anzahl_zeilen: int = anzahl_paare*2 // anzahl_spalten +1





class Karte:

    def __init__(self, symbol: str, farbe: str):
        self.symbol = symbol      # Vorderseite
        self.farbe  = farbe       # Rückseite
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

    def __init__(self, karte_vorne: tuple[str, ...], karte_hinten: tuple[str, str]):
        self.paarestapel: list[Karte] = []
        for hinten in karte_hinten:
            for vorne in karte_vorne:
                self.paarestapel.append(Karte(vorne, hinten))

        random.shuffle(self.paarestapel)


    def spielfeld(self):
        os.system('clear')

        paare = [k.sichtbar() for k in self.paarestapel]
        print("paare: ", *paare)
        print("Index:  ", end=" ")
        for i in range(len(paare)):
            print(f"{i:2}", end=" ")
        print("\n")

    def spielen(self):
        while any(k.aufgedeckt() == False for k in self.paarestapel):
            self.spielfeld()
            try:
                i, j = map(int, input("Welche zwei paare möchten Sie aufdecken (z. B. 0 1)? ").split())
            except ValueError as e:
                print("Bitte zwei Zahlen eingeben.", e)
                time.sleep(1.5)
                continue

            if i < 0 or i >= len(self.paarestapel) or j < 0 or j >= len(self.paarestapel) or i == j:
                print("Ungültige Indizes.")
                time.sleep(1.5)
                continue

            if self.paarestapel[i].aufgedeckt() == True or self.paarestapel[j].aufgedeckt() == True:
                print("Diese Karte ist schon aufgedeckt.")
                time.sleep(1.5)
                continue

            self.paarestapel[i].aufdecken()
            self.paarestapel[j].aufdecken()

            self.spielfeld()


            if self.paarestapel[i].vergleichen(self.paarestapel[j]):
                print("Paar gefunden!")

            else:
                print("Kein Paar.")
                self.paarestapel[i].zudecken()
                self.paarestapel[j].zudecken()
            time.sleep(1.5)

        print("Glückwunsch! Du hast alle Paare gefunden.")




m1 = Memory(("🐍", "🐢", "🐸"), ("🟦", "🟥"))
m1.spielen()


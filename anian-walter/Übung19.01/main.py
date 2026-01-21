import random
import time
import os

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
        self.stapel: list[Karte] = []
        for hinten in karte_hinten:
            for vorne in karte_vorne:
                self.stapel.append(Karte(vorne, hinten))

        random.shuffle(self.stapel)


    def spielfeld(self):
        os.system('cls')

        karten = [k.sichtbar() for k in self.stapel]
        print("Karten: ", *karten)
        print("Index:  ", end=" ")
        for i in range(len(karten)):
            print(f"{i:2}", end=" ")
        print("\n")

    def spielen(self):
        while any(k.aufgedeckt() == False for k in self.stapel):
            self.spielfeld()
            try:
                i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
            except ValueError as e:
                print("Bitte zwei Zahlen eingeben.", e)
                time.sleep(1.5)
                continue

            if i < 0 or i >= len(self.stapel) or j < 0 or j >= len(self.stapel) or i == j:
                print("Ungültige Indizes.")
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


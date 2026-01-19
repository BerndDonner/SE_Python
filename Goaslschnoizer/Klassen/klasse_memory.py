import random
import os
import time

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

    def vergleichen(self, andere: 'Karte') -> bool:
        return self.symbol == andere.symbol

    def sichtbar(self) -> str:
        if self._aufgedeckt: return self.symbol
        return self.farbe

class Memory:
    def __init__(self, karte_vorne: tuple[str,...], karte_hinten: tuple[str,str]):
        self.kombis = list()
        for hinten in karte_hinten:
            for vorne in karte_vorne:
                self.kombis.append(Karte(vorne, hinten))

        random.shuffle(self.kombis)

    def spielfeld(self):
        os.system('cls')
        karten = [k.sichtbar() for k in  self.kombis]
        print("Karten: ", *karten)
        print("Index:  ", end=" ")
        for i in range(len(karten)):
            print(f"{i:2}", end=" ")
        print("\n")
    
    def spielen(self):
        while any(k.aufgedeckt() == False for k in self.kombis):
            self.spielfeld()
            try:
                i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
            except ValueError as e:
                print("Bitte zwei Zahlen eingeben.", e)
                time.sleep(3)
                continue

            if i < 0 or i >= len(self.kombis) or j < 0 or j >= len(self.kombis) or i == j:
                print("Ungültige Indizes.")
                time.sleep(3)
                continue

            if self.kombis[i].aufgedeckt() == True or self.kombis[j].aufgedeckt() == True:
                print("Diese Karte ist schon aufgedeckt.")
                time.sleep(3)
                continue

            self.kombis[i].aufdecken()
            self.kombis[j].aufdecken()

            self.spielfeld()


            if self.kombis[i].vergleichen(self.kombis[j]):
                print("Paar gefunden!")
                time.sleep(3)

            else:
                print("Kein Paar.")
                self.kombis[i].zudecken()
                self.kombis[j].zudecken()
                time.sleep(3)

        print("Glückwunsch! Du hast alle Paare gefunden.")

m1 = Memory(("🐍", "🐢", "🐸"),("🟦", "🟥"))
m1.spielen()


    

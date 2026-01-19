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



def spielfeld():
    os.system("cls")

    karten = [k.sichtbar() for k in kombis]
    print("Karten: ", *karten)
    print("Index:  ", end=" ")
    for i in range(len(karten)):
        print(f"{i:2}", end=" ")
    print("\n")

karte_vorne = ("🐍", "🐢", "🐸")
karte_hinten = ("🟦", "🟥")

kombis = list()
for hinten in karte_hinten:
    for vorne in karte_vorne:
        kombis.append(Karte(vorne, hinten))

random.shuffle(kombis)

while any(k.aufgedeckt() == False for k in kombis):
    spielfeld()
    try:
        i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
    except ValueError as e:
        print("Bitte zwei Zahlen eingeben.", e)
        time.sleep(1.5)
        continue

    if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j:
         print("Ungültige Indizes.")
         time.sleep(1.5)
         continue

    if kombis[i].aufgedeckt() == True or kombis[j].aufgedeckt() == True:
        print("Diese Karte ist schon aufgedeckt.")
        time.sleep(1.5)
        continue

    kombis[i].aufdecken()
    kombis[j].aufdecken()

    spielfeld()


    if kombis[i].vergleichen(kombis[j]):
        print("Paar gefunden!")

    else:
        print("Kein Paar.")
        kombis[i].zudecken()
        kombis[j].zudecken()
    time.sleep(1.5)

print("Glückwunsch! Du hast alle Paare gefunden.")
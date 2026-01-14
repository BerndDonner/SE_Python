import random
import os
import time
def spielfeld():
    time.sleep(1.5)
    os.system('cls')
    karten = [k.zeigen() for k in kombis]
    print("Karten: ", *karten)
    print("Index:  ", end=" ")
    for i in range(len(karten)):
        print(f"{i:2}", end=" ")
    print("\n")



class Karte:
    def __init__(self, symbol, farbe):
        self.symbol = symbol
        self.farbe = farbe
        self._aufgedeckt = False

    def aufdecken(self):
        self._aufgedeckt = True

    def ist_aufgedeckt(self):
        return self._aufgedeckt

    def zuklappen(self):
        self._aufgedeckt = False

    def vergleichen(self, andere: 'Karte')-> bool:
        return self.symbol == andere.symbol
    
    def zeigen(self)-> str:
        return self.symbol if self._aufgedeckt else self.farbe

karte_vorne = ("🐍", "🐢", "🐸")
karte_hinten = ("🟦", "🟥")
kombis = list()
for hinten in karte_hinten:
    for vorne in karte_vorne:

        kombis.append(Karte(vorne, hinten))

random.shuffle(kombis) 


while any(k.ist_aufgedeckt() == False for k in kombis):
    spielfeld()
    try:
        i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
    except ValueError:
        print("Bitte zwei Zahlen eingeben.")
        continue

    if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j:
        print("Ungültige Indizes.")
        continue

    if kombis[i].ist_aufgedeckt() == True or kombis[j].ist_aufgedeckt() == True:
        print("Diese Karte ist schon aufgedeckt.")
        continue

    kombis[i].aufdecken()
    kombis[j].aufdecken()

    spielfeld()

    if kombis[i].vergleichen(kombis[j]):
        print("Paar gefunden!")

    else:
        print("Kein Paar.")
        kombis[i].zuklappen()
        kombis[j].zuklappen()

print("Glückwunsch! Du hast alle Paare gefunden.")
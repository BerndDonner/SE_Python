import random
import time
import os
import sys

class Karte:
    def __init__(self, symbol, farbe):
        self.symbol = symbol
        self.farbe = farbe
        self._aufgedeckt = False 
   

    def aufdecken(self):
        self._aufgedeckt = True

    def aufgedeckt(self)->bool:
        return self._aufgedeckt    

    def verdecken(self):
        self._aufgedeckt = False

    def sichtbar(self): 
        if self._aufgedeckt:
            return self.symbol
        else:
            return self.farbe
        
    def vergleichen(self, other: 'Karte'):
                        # # if self.symbol == other.symbol:
                        #     return True
                        # else:   
                        #     return False
        return self.symbol == other.symbol

class MemorySpiel:  
    def __init__(self, karte_vorne: tuple[str, ...], karte_hinten: tuple[str, str]):
        self.kartenstapel = list()
        for hinten in karte_hinten:
            for vorne in karte_vorne:
               self.kartenstapel.append(Karte(vorne,hinten ))
        random.shuffle(self.kartenstapel)

    def spielfeld(self):
        #bildschirmlöschen:
        os.system('cls')
        print("______________________________________ MEMORY____________________________________________")
        karten = [k.sichtbar() for k in self.kartenstapel]
        print("Karten: ", *karten)
        print("Index:  ", end=" ")
        for i in range(len(karten)):
            print(f"{i:2}", end=" ")
        print("\n")

    def spielen(self):
        while any(k.aufgedeckt() == False for k in self.kartenstapel): 
            self.spielfeld()
            try:
                i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
            except ValueError:
                print("Bitte zwei Zahlen eingeben.")
                time.sleep(1.5)
                continue

            if i < 0 or i >= len(self.kartenstapel) or j < 0 or j >= len(self.kartenstapel) or i == j:
                print("Ungültige Indizes.")
                time.sleep(1.5)
                continue

            if self.kartenstapel[i].aufgedeckt() or self.kartenstapel[j].aufgedeckt():
                print("Diese Karte ist schon aufgedeckt.")
                time.sleep(1.5)
                continue

            self.kartenstapel[i].aufdecken()
            self.kartenstapel[j].aufdecken()

            self.spielfeld()

            if self.kartenstapel[i].vergleichen(self.kartenstapel[j]):
                print("Paar gefunden!")
                time.sleep(1.5)

            else:
                print("Kein Paar.")
                self.kartenstapel[i].verdecken()
                self.kartenstapel[j].verdecken()
                time.sleep(1.5)
            
        print("Glückwunsch! Du hast alle Paare gefunden.")





                    



m1= MemorySpiel(("🐍", "🐢", "🐸", "🐶"),("🟦", "🟥"))#, "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯", "🦁")
m1.spielen()





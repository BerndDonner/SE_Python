import random
import time
import os



class XY:
    def __init__(self, anzahl_paare: int, anzahl_spalten: int):
        # Input Validierung
        assert anzahl_paare > 0, "Die Anzahl der Paare muss größer als 0 sein."
        assert isinstance(anzahl_paare, int), "Die Anzahl der Paare muss eine ganze Zahl sein."
        assert anzahl_spalten > 0, "Die Anzahl der Spalten muss größer als 0 sein."
        assert isinstance(anzahl_spalten, int), "Die Anzahl der Spalten muss eine ganze Zahl sein."
        anzahl_zeilen = (anzahl_paare*2)+(anzahl_spalten-1) // anzahl_spalten
        for y in range(anzahl_zeilen):
            for x in range(anzahl_spalten):
                print(chr(ord('A') + x), y)



class Karte:
    def  lf.symbol = symbol
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
    def __init__(self, karte_vorne: tuple[str, ...], karte_hinten: tuple[str, str], counter: int = 0):
        self.kartenstapel = list()
        self.counter = counter
        for hinten in karte_hinten:
            for vorne in karte_vorne:
               self.kartenstapel.append(Karte(vorne,hinten ))
        random.shuffle(self.kartenstapel)

    def spielfeld(self):
        #bildschirmlöschen:
        os.system('cls')
        print("____________________________________________ MEMORY________________________________________________________")
        print("\n")
        karten = [k.sichtbar() for k in self.kartenstapel]
        print("Karten: ", *karten)
        print("Index:  ", end=" ")  
        for i in range(len(karten)):
            print(f"{i:2}", end=" ")
        print("\n")
        print("Versuche:  ", self.counter)
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
                self.counter += 1
                time.sleep(1.5)

            else:
                print("Kein Paar.")
                self.kartenstapel[i].verdecken()
                self.kartenstapel[j].verdecken()
                self.counter += 1
                time.sleep(1.5)

    
            
        print("Glückwunsch! Du hast alle Paare in", self.counter, "Versuchen gefunden.")





                    

test = XY(8, 3)

m1= MemorySpiel(("🐍", "🐢", "🐸", "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯", "🦁"),("🟦", "🟥"))
m1.spielen()




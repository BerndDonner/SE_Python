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

def restart_program():
    """Startet das aktuelle Programm neu und ersetzt den aktuellen Prozess."""
    print("Programm wird neu gestartet...")
    time.sleep(0.5)
   # sys.executable ist der Pfad zum Python-Interpreter (z.B. python.exe)
    # sys.argv[0] ist der Name des aktuellen Skripts
    os.execv(sys.executable, [sys.executable] + sys.argv)


                    
def spielfeld():
    #bildschirmlöschen:
    os.system('cls')
    print("______________________________________ MEMORY____________________________________________")
    karten = [k.sichtbar() for k in kartenstapel]
    print("Karten: ", *karten)
    print("Index:  ", end=" ")
    for i in range(len(karten)):
        print(f"{i:2}", end=" ")
    print("\n")


karte_vorne = ("🐍", "🐢", "🐸", "🐶")#, "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯", "🦁")
karte_hinten = ("🟦", "🟥")
 
kartenstapel = list()
for hinten in karte_hinten:
    for vorne in karte_vorne:
          kartenstapel.append(Karte(vorne,hinten ))

random.shuffle(kartenstapel)

while any(k.aufgedeckt() == False for k in kartenstapel): 
    spielfeld()
    try:
        i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
    except ValueError:
        print("Bitte zwei Zahlen eingeben.")
        time.sleep(1.5)
        continue

    if i < 0 or i >= len(kartenstapel) or j < 0 or j >= len(kartenstapel) or i == j:
        print("Ungültige Indizes.")
        time.sleep(1.5)
        continue

    if kartenstapel[i].aufgedeckt() in karte_vorne or kartenstapel[j].aufgedeckt() in karte_vorne:
        print("Diese Karte ist schon aufgedeckt.")
        time.sleep(1.5)
        continue

    kartenstapel[i].aufdecken()
    kartenstapel[j].aufdecken()

    spielfeld()

    if kartenstapel[i].vergleichen(kartenstapel[j]):
        print("Paar gefunden!")
        time.sleep(1.5)

    else:
        print("Kein Paar.")
        kartenstapel[i].verdecken()
        kartenstapel[j].verdecken()
        time.sleep(1.5)
       
print("Glückwunsch! Du hast alle Paare gefunden.")
time.sleep(3)
eingabe = False
x = 2
while eingabe == False:
   
    neues_spiel = input("Neues Spiel y/n? ")  # Eingabe bereinigen und in Kleinbuchstaben umwandeln
    if neues_spiel == "y" or neues_spiel == "Y":
        restart_program()
        eingabe = True
    elif neues_spiel == "n" or neues_spiel ==  "N":
        print("Danke fürs Spielen!")
        time.sleep(2)
        eingabe = True
        sys.exit()
    else:
        print(f"Ungültige Eingabe. Das Programm wird für {x} Sekunden stillstehen.")
        time.sleep(x)
        x = x*x
        eingabe = False
 
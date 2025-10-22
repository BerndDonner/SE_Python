
import random


Karten_alle = "🌟😊🎉🔥🌍🌟😊🎉🔥🌍" 
Karten=list(Karten_alle)   
Karten_pos = [f"{i+1:2}" for i in range(len(Karten))]
random.shuffle(Karten)
print(Karten)
print(Karten_pos)
versteckt = ["❓"] * len(Karten)
print(versteckt)
while "❓" in versteckt:
    auswahl = input("Zwei Karten auswählen (z.B. 1 2): ")
    karte1, karte2 = auswahl.split()
    print(karte1)
    print(karte2)
    karte1 = int(karte1) - 1
    karte2 = int(karte2) - 1
    versteckt[karte1] = Karten[karte1]
    versteckt[karte2] = Karten[karte2]
    if versteckt[karte1] == versteckt[karte2]:
        print(versteckt)
        print("Treffer!")
    else:
        print(versteckt)
        input("Keine Übereinstimmung. Drücke Enter, um die Karten zu verbergen.")
        versteckt[karte1] = "❓"
        versteckt[karte2] = "❓"
    print(versteckt)
print("Glückwunsch! Du hast alle Paare gefunden.")

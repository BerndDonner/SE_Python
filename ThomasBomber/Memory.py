import random


Karten_alle = ("😀","🎉","🌍","🚀","🍕","🐶","📚","🎶","💡","❤️","🔥","🌈","😴","🧠","🕹️","🏆","💻","📸","🌻","⏰")
anzahlkarten = input("Wie viele Kartenpaare möchtest du spielen? (Maximal 10): ")
try:
    anzahlkarten = int(anzahlkarten)
    if anzahlkarten < 1 or anzahlkarten > 10:
        print("Bitte eine Zahl zwischen 1 und 10 eingeben.")
        exit()
except ValueError:
    print("Ungültige Eingabe: bitte eine Zahl eingeben.")
    exit()
tmp = list(Karten_alle)
print(tmp)
random.shuffle(tmp)
Karten_ausgewaehlt =tmp[:anzahlkarten]
Karten_rueckseite=["🟦"]*len(Karten_ausgewaehlt)
for i in range(len(Karten_ausgewaehlt)):
    Karten_rueckseite.append("🟥")
Karten=list(Karten_ausgewaehlt*2)
Karten_pos = [f"{i+1:2}" for i in range(len(Karten))]
random.shuffle(Karten)


print(Karten_pos)

#versteckt = ["❓"] * len(Karten)
#🟦🟥
print(Karten_rueckseite)


while ("🟥") in Karten_rueckseite:
    auswahl = input("Zwei Karten auswählen (z.B. 1 2): ")
    parts = auswahl.split()
    if len(parts) != 2:
        print("Bitte genau zwei Zahlen durch Leerzeichen getrennt eingeben.")
        continue
    try:
        karte1, karte2 = map(int, parts)
    except ValueError:
        print("Ungültige Eingabe: bitte Zahlen eingeben.")
        continue
    karte1 -= 1
    karte2 -= 1
    Karten_rueckseite[karte1] = Karten[karte1]
    Karten_rueckseite[karte2] = Karten[karte2]
    if Karten_rueckseite[karte1] == Karten_rueckseite[karte2]:
        print(Karten_rueckseite)
        print("Treffer!")
    else:
        print(Karten_rueckseite)
        input("Keine Übereinstimmung. Drücke Enter, um die Karten zu verbergen.")
        Karten_rueckseite[karte1] = "❓"
        Karten_rueckseite[karte2] = "❓"
    print(Karten_rueckseite)
print("Glückwunsch! Du hast alle Paare gefunden.")

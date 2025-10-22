import random
Karten_alle = "🙂 🌍 🚀 🎶 🍀 "
Memory = (Karten_alle.split())*2
random.shuffle(Memory)
Zahlen = [F"{i+1:2}"for i in range(len(Memory))]
print("Willkommen zum Memory-Spiel!")
print("Finde die Paare!")
Spiel = ['❓'] * len(Memory)
print(Spiel)    
print(Zahlen)

while '❓' in Spiel:
    print("Wähle zwei Karten zum Aufdecken (1-10):")
    Karte_1, Karte_2 = input().split()
    Karte_1 = int(Karte_1) - 1
    Karte_2 = int(Karte_2) - 1

    # Ungültige Eingaben abfangen
    if Karte_1 == Karte_2 or not (0 <= Karte_1 < len(Memory)) or not (0 <= Karte_2 < len(Memory)):
        print("Ungültige Auswahl. Bitte zwei verschiedene gültige Zahlen eingeben.")
        continue

    Spiel[Karte_1] = Memory[Karte_1]
    Spiel[Karte_2] = Memory[Karte_2]
    print(Spiel)

    if Memory[Karte_1] == Memory[Karte_2]:
        print("Paar gefunden!")
    else:
        print("Kein Paar. Versuche es erneut.")
        Spiel[Karte_1] = '❓'
        Spiel[Karte_2] = '❓'
    print(Spiel)

print("Glückwunsch, alle Paare gefunden!")
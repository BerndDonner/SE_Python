import random
Karten_alle = ("🌹", "🐸", "🦋", "🍊" ,"⭐",
               "🌊", "🍀", "🦄", "🍎", "🌈",
               "🌻", "🐠", "🧡", "🐝", "🍇",
               "🔥", "🐧", "🌙", "🍋", "⚡")
print("Mit wie vielen Paaren möchtest du spielen? (Maximal 20)")
Anzahl_Paare = int(input())
Memory = Karten_alle[:Anzahl_Paare] * 2
Zahlen = (f"{i+1:2}"for i in range(len(Memory)))
print("Willkommen zum Memory-Spiel!")
print("Finde die Paare!")
Spiel = ['❓'] * len(Memory)
for i, s in enumerate(Memory):
    zaehler[s] = zaehler.get(s, 0) + 1  # Vorkommen hochzählen
    if zaehler[s] % 2 == 0:
print(Spiel)    
print(Zahlen)

while '❓' or '❔' in Spiel:
    print(f"Wähle zwei Karten zum Aufdecken (1-{len(Memory)}):")
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
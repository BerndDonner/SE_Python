import random
karte_vorne = ("🐍", "🐢", "🐸")
karte_hinten  = ("🟦", "🟥")

kombis = []
for hinten in karte_hinten:
    for vorne in karte_vorne:
        kombis.append((hinten, vorne))    

random.shuffle(kombis)
karten = [tupel[0] for tupel in kombis]
Zahlen = (f"{i+1:2}"for i in range(len(karten)))
print("Willkommen bei Memory!")
while '🟥' or '🟦' in karten:
    print(*karten)
    print(*Zahlen)
    print("Wähle zwei Karten zum Aufdecken (1-6):")
    Karte_1, Karte_2 = input().split()      
    Karte_1 = int(Karte_1) - 1
    Karte_2 = int(Karte_2) - 1
    if karten[Karte_1][1] == karten[Karte_2][1]:
        print("Paar gefunden!")
    else:
        print("Kein Paar. Versuche es erneut.")

    print(karten)

print("Glückwunsch, alle Paare gefunden!")
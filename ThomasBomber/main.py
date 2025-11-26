import random

def spielfeld():
    karten = [tupel[0] for tupel in kombis]
    print("Karten: ", *karten)
    print("Index:  ", end=" ")
    for i in range(len(karten)):
        print(f"{i:2}", end=" ")
    print("\n")

karte_vorne = ("🐍", "🐢", "🐸")
karte_hinten = ("🟦", "🟥")

kombis = []
for hinten in karte_hinten:
    for vorne in karte_vorne:
        kombis.append((hinten, vorne))

random.shuffle(kombis)

while any(sichtbar in karte_hinten for sichtbar, _ in kombis): 
    spielfeld()
    try:
        i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
    except ValueError:
        print("Bitte zwei Zahlen eingeben.")
        continue

    # if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j:
    #     print("Ungültige Indizes.")
    #     continue

    if kombis[i][0] in karte_vorne or kombis[j][0] in karte_vorne:
        print("Diese Karte ist schon aufgedeckt.")
        continue

    a, b = kombis[i]
    kombis[i] = (b, a)

    a, b = kombis[j]
    kombis[j] = (b, a)

    spielfeld()

    if kombis[i][0] == kombis[j][0]:
        print("Paar gefunden!")

    else:
        print("Kein Paar.")
        a, b = kombis[i]
        kombis[i] = (b, a)

        a, b = kombis[j]
        kombis[j] = (b, a)

print("Glückwunsch! Du hast alle Paare gefunden.")
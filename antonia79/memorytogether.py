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
nochmal = True

kombis = []
for hinten in karte_hinten:
    for vorne in karte_vorne:
        kombis.append((hinten, vorne))

random.shuffle(kombis)

verdeckt = [tupel[0] for tupel in kombis]
while any(tupel[0] in karte_hinten for tupel in kombis):
    spielfeld()

    i, j = input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split()

    i = int(i)
    j = int(j)

    if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j:
        print("Ungültige Indizes.")

    a, b = kombis[i]
    kombis[i] = (b, a)

    a, b = kombis[j]
    kombis[j] = (b, a)

    spielfeld()

    if kombis[i][0] == kombis[j][0]:
        print("Ein Paar!")
    else: 
        print("Neuer Versuch ")
        b, a = kombis[i]
        kombis[i] = (a, b)

        b, a = kombis[j]
        kombis[j] = (a, b)

    

print("Du hast alle Paare gefunden!")
nochmal = input("Magst du nochmal spielen? (True oder False)").split()

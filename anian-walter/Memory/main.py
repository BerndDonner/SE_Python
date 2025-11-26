import random

def spielfeld():
    karten = [tupel[0] for tupel in kombis]
    print("Karten: ", *karten)
    print("Index:  ", end=" ")
    for i in range(len(karten)):
        print(f"{i:2}", end=" ")
    print("\n")

def karten_lesen_und_vergleichen():
    i, j = input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split()
    i = int(i)
    j = int(j)
    if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j or kombis[i] == karte_vorne or kombis[j] == karte_vorne:
        print("Ungültige Indizes.")
    else:
        a, b = kombis[i]
        kombis[i] = (b, a)
        a, b = kombis[j]
        kombis[j] = (b, a)

    spielfeld()

    if kombis[i][0] == kombis[j][0]:
        print("Treffer!")
    else:
        print("Leider kein Treffer.")   
        a, b = kombis[i]
        kombis[i] = (b, a)      
        a, b = kombis[j]
        kombis[j] = (b, a)

karte_vorne = ("🐍", "🐢", "🐸")
karte_hinten  = ("🟦", "🟥")

kombis = []
for hinten in karte_hinten:
    for vorne in karte_vorne:
        kombis.append((hinten, vorne))    

random.shuffle(kombis)

while any(kartenseite in karte_hinten for kartenseite in [tupel[0] for tupel in kombis]):
    spielfeld()
    karten_lesen_und_vergleichen()
print("Glückwunsch, alle Paare gefunden!")
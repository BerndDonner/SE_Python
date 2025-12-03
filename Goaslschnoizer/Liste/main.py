import random

def spielfeld():
    karten = [tupel[0] for tupel in kombis]
    print("Karten: ", *karten)
    print("Index:  ", end=" ")
    for i in range(len(karten)):
        print(f"{i+1:2}", end=" ")
    print("\n")

karte_vorne = ("🐍", "🐢", "🐸")
karte_hinten = ("🎴", "🃏")

kombis = []
for hinten in karte_hinten:
    for vorne in karte_vorne:
        kombis.append((hinten, vorne))

random.shuffle(kombis)

verdeckt = [True] * len(kombis)
while any(verdeckt):
    spielfeld()

    #i, j = input("Welche zwei Karten möchten Sie aufdecken (z. B.: 1 2)? ").split()       #Karten gemeinsam abfragen
    i = input("Welche erste Karte möchten Sie aufdecken (z. B.: 1)? ")                     #Karten einzeln abfragen
    j = input("Welche zweite Karte möchten Sie aufdecken (z. B.: 2)? ")

    i = int(i) -1
    j = int(j) -1

    if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j:
        print("Ungültige Indizes.")


    a, b = kombis[i]
    kombis[i] = (b, a)

    a, b = kombis[j]
    kombis[j] = (b, a)

    spielfeld()

    if kombis[i][0] == kombis[j][0]:
        print("Treffer! Die Karten bleiben aufgedeckt.")
        verdeckt[i] = False
        verdeckt[j] = False
    else:
        print("Leider kein Treffer. Die Karten werden wieder umgedreht.")
        a, b = kombis[i]
        kombis[i] = (b, a)
        a, b = kombis[j]
        kombis[j] = (b, a)
    
   
print("Herzlichen Glückwunsch! Sie haben alle Karten aufgedeckt.")
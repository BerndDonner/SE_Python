import random

def spielfeld():
    karten = [tupel[0] if tupel else "  " for tupel in kombis]
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

# Game-Loop
while True:
    spielfeld()

    i, j = input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split()

    i = int(i)
    j = int(j)

    if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j:
        print("Ungültige Indizes.")
        # Karten zurückdrehen bei falscher Eingabe
        if i >= 0 and i < len(kombis) and kombis[i] is not None:
            a, b = kombis[i]
            kombis[i] = (b, a)
        if j >= 0 and j < len(kombis) and kombis[j] is not None:
            a, b = kombis[j]
            kombis[j] = (b, a)
        continue
    
    # TODO: überprüfen das Karten nich offen sind

    a, b = kombis[i]
    kombis[i] = (b, a)

    a, b = kombis[j]
    kombis[j] = (b, a)

    spielfeld()

    # Überprüfen ob es ein Paar ist
    if kombis[i][0] == kombis[j][0]:  # Vorderseiten vergleichen (jetzt an Index 0)
        print("Paar-Gefunden")
        # Karten aufgedeckt liegenlassen (nicht entfernen)
    else:
        print("Kein Paar")
        # Karten zurückdrehen
        a, b = kombis[i]
        kombis[i] = (b, a)
        a, b = kombis[j]
        kombis[j] = (b, a)

import random

def spielfeld():
    karten = []
    for idx, tupel in enumerate(kombis):
        if aufgedeckt[idx]:
            # Aufgedeckt: Vorderseite anzeigen
            karten.append(tupel[1])
        else:
            # Verborgen: Rückseite anzeigen
            karten.append(tupel[0])
    print("Karten: ", *karten)
    print("Index:  ", end=" ")
    for i in range(len(karten)):
        print(f"{i:2}", end=" ")
    print("\n")

karte_vorne = ("🐍", "🐢", "🐸")
karte_hinten = ("🟦", "🟥")

# Spiel initialisieren
def init_spiel():
    global kombis, aufgedeckt
    kombis = []
    for hinten in karte_hinten:
        for vorne in karte_vorne:
            kombis.append((hinten, vorne))
    aufgedeckt = [False] * len(kombis)
    random.shuffle(kombis)

init_spiel()

# Game-Loop
while True:
    spielfeld()

    try:
        i, j = input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split()

        i = int(i)
        j = int(j)
    except ValueError:
        print("Ungültige Eingabe. Bitte zwei Zahlen eingeben.")
        continue

    if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j:
        print("Ungültige Indizes.")
        continue
    
    # TODO: überprüfen das Karten nich offen sind

    aufgedeckt[i] = True
    aufgedeckt[j] = True

    spielfeld()

    # Überprüfen ob es ein Paar ist
    if kombis[i][1] == kombis[j][1]:  # Vorderseiten vergleichen
        print("Paar-Gefunden")
        # Karten bleiben aufgedeckt
    else:
        print("Kein Paar")
        # Karten zurückdrehen
        aufgedeckt[i] = False
        aufgedeckt[j] = False


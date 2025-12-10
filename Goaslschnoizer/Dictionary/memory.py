import random

def spielfeld():
    karten = [k[k["sichtbar"]] for k in kombis]
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
        karte = {}
        karte["vorne"] = vorne
        karte["hinten"] = hinten
        karte["sichtbar"] = "hinten"

        kombis.append(karte)

random.shuffle(kombis)

verdeckt = [True] * len(kombis)
while any(verdeckt):
    spielfeld()

    try: #i, j = input("Welche zwei Karten möchten Sie aufdecken (z. B.: 1 2)? ").split()       #Karten gemeinsam abfragen
        i = input("Welche erste Karte möchten Sie aufdecken (z. B.: 1)? ")                     #Karten einzeln abfragen
        j = input("Welche zweite Karte möchten Sie aufdecken (z. B.: 2)? ")

        i = int(i) -1
        j = int(j) -1

        assert i >= 0 and i < len(kombis) and j >= 0 and j < len(kombis) and i != j

    except ValueError as e:
        print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.",e)
        continue
    
    except IndexError as e:
        print("Ungültige Eingabe. Bitte gültige Indizes eingeben.",e)
        continue

    except AssertionError as e:
        print("Ungültige Eingabe. Bitte gültige Indizes eingeben.",e)
        continue

    #if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j:          #möglichkeit wie asseertion
        print("Ungültige Indizes.")
        continue


    kombis[i]["sichtbar"] = "vorne"
    kombis[j]["sichtbar"] = "vorne"
    

    spielfeld()

    if kombis[i]["vorne"] == kombis[j]["vorne"]:
        print("Treffer! Die Karten bleiben aufgedeckt.")
        verdeckt[i] = False
        verdeckt[j] = False
    else:
        print("Leider kein Treffer. Die Karten werden wieder umgedreht.")
        kombis[i]["sichtbar"] = "hinten"
        kombis[j]["sichtbar"] = "hinten"
    
   
print("Herzlichen Glückwunsch! Sie haben alle Karten aufgedeckt.")
def print_karten():
    karten = [tupel[0] for tupel in Karten_kombi]
    print("Karten: ", *karten, sep= "  ", end="\n")
    print("Index: ", end = " ")
    for i, _ in enumerate(karten, start=1):
        print(f" {i:2}", end=" ")
    print("\n")
##############################################################################    
import random   
##############################################################################
Karten_alle = ("🐶","🐱","🐭","🐹","🐰","🦊","🐻","🐼","🐨","🐯")
Karte_verdeckt = ("🎴","🀄")
##############################################################################
Karten_kombi = []
for hinten in Karte_verdeckt:
    for vorne in Karten_alle:
        Karten_kombi.append( (hinten, vorne) )
print(*Karten_kombi)
random.shuffle(Karten_kombi)
###############################################################################
aufgedeckte = [tupel[0] for tupel in Karten_kombi]
while Karte_verdeckt[0] in aufgedeckte:
    print_karten() 
    h, j = input("\nZwei Karten zum Aufdecken eingeben: ").split() 
    h=int(h)
    j=int(j)
    h-=1
    j-=1
    if h<0 or h>=len(Karten_kombi) or j<0 or j>=len(Karten_kombi) or h==j:
        print("Ungültige Eingabe") 
    #else falls karten schon aufgedeckt sind
    a, b = Karten_kombi[h]
    Karten_kombi[h] = (b, a)
    a, b = Karten_kombi[j]
    Karten_kombi[j] = (b, a)
    print_karten()
    if Karten_kombi[h][0] == Karten_kombi[j][0]:
        print("Treffer!")  
    else:
        print("Leider kein Treffer.")  
        a, b = Karten_kombi[h]
        Karten_kombi[h] = (b, a)
        a, b = Karten_kombi[j]
        Karten_kombi[j] = (b, a)
    aufgedeckte = [tupel[0] for tupel in Karten_kombi]
##############################################################################
print("Herzlichen Glückwunsch, Sie haben alle Karten aufgedeckt!")
##############################################################################
##############################################################################



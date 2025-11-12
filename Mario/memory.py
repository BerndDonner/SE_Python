import random   

Karten_alle = ("🐶","🐱","🐭")#,"🐹","🐰","🦊","🐻","🐼","🐨","🐯")
Karte_verdeckt = ("🎴","🀄")

Karten_kombi = []
for hinten in Karte_verdeckt:
    for vorne in Karten_alle:
        Karten_kombi.append( (hinten, vorne) )
print(*Karten_kombi)

random.shuffle(Karten_kombi)
print(*Karten_kombi)
karten = [tupel[0] for tupel in Karten_kombi]
print("Karten: ", *karten)
print("Index: ", end = " ")
for i in range(len(karten)):
    print(f"{i:2}", end=" ")
i, j = input("\nZwei Karten zum Aufdecken eingeben: ").split() 
i=int(i)
j=int(j)

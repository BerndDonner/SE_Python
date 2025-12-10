import random
def main():
    def spielfeld():
        karten = [k[k["sichtbar"]] for k in kombis]
        print("Karten: ", *karten)
        print("Index:  ", end=" ")
        for i in range(len(karten)):
            print(f"{i:2}", end=" ")
        print("\n")

    def karten_lesen_und_vergleichen():
        i, j = input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split()
        i = int(i)
        j = int(j)
        if i >= 0 and i < len(kombis) and j >= 0 and j < len(kombis) and j != i and kombis[i]["sichtbar"] != "vorne" and kombis[j]["sichtbar"] != "vorne" and kombis[i]["hinten"] != kombis[j]["hinten"]: 
            kombis[i]["sichtbar"] = "vorne"
            kombis[j]["sichtbar"] = "vorne"
        else:
            print("Ungültige Indizes.")
            karten_lesen_und_vergleichen()

        if kombis[i]["vorne"] == kombis[j]["vorne"]:
            print("Treffer!")
        else:
            print("Leider kein Treffer.") 
            spielfeld()
            kombis[i]["sichtbar"] = "hinten"
            kombis[j]["sichtbar"] = "hinten"  



    karte_vorne = ("🐍", "🐢", "🐸")
    karte_hinten  = ("🟦", "🟥")

    kombis = []
    for hinten in karte_hinten:
        for vorne in karte_vorne:
            karte = {}
            karte['vorne'] = vorne
            karte['hinten'] = hinten
            karte["sichtbar"] = "hinten"    
            kombis.append(karte)


    random.shuffle(kombis)

    while any(k["sichtbar"] != "vorne" for k in kombis):
        spielfeld()
        karten_lesen_und_vergleichen()
    spielfeld()
    print("Glückwunsch, alle Paare gefunden!")
    if "1" == input("Drücke 1 um neu zu starten."):
        main()
main()
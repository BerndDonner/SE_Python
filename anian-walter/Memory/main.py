import random

class Karte:

    def __init__(self, symbol: str, farbe: str):
        self.symbol = symbol
        self.farbe = farbe
        self._aufgedeckt = False

    def aufdecken(self) -> None:
        self._aufgedeckt = True

    def aufgedeckt(self) -> bool:
        return self._aufgedeckt
    
    def zudecken(self) -> None:
        self._aufgedeckt = False

    def vergleichen(self, andere: 'Karte') -> bool:
        return self.symbol == andere.symbol

    def sichtbar(self) -> str:
        if self._aufgedeckt: return self.symbol
        return self.farbe


def main():
    def spielfeld():
        karten = [k.sichtbar() for k in kombis]
        print("Karten: ", *karten)
        print("Index:  ", end=" ")
        for i in range(len(karten)):
            print(f"{i:2}", end=" ")
        print("\n")

    def karten_lesen_und_vergleichen():
        i, j = input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split()
        i = int(i)
        j = int(j)
        if i >= 0 and i < len(kombis) and j >= 0 and j < len(kombis) and j != i and kombis[i].aufgedeckt() != "vorne" and kombis[j].aufgedeckt() != "vorne": 
            kombis[i].aufdecken()
            kombis[j].aufdecken()
        else:
            print("Ungültige Indizes.")
            karten_lesen_und_vergleichen()

        if kombis[i].vergleichen(kombis[j]):
            print("Treffer!")
        else:
            print("Leider kein Treffer.") 
            spielfeld()
            kombis[i].zudecken()
            kombis[j].zudecken()



    karte_vorne = ("🐍", "🐢", "🐸")
    karte_hinten  = ("🟦", "🟥")

    kombis = list()
    for hinten in karte_hinten:
        for vorne in karte_vorne:
            kombis.append(Karte(vorne, hinten))

    random.shuffle(kombis)

    while any(k.aufgedeckt() == False for k in kombis):
        spielfeld()
        karten_lesen_und_vergleichen()
    spielfeld()
    print("Glückwunsch, alle Paare gefunden!")
    if "1" == input("Drücke 1 um neu zu starten. "):
        main()
main()
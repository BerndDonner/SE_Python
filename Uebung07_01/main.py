import random

class Karte:

    def __init___(self, symbol: str, farbe: str):
        self.symbol = symbol      # Vorderseite
        self.farbe  = farbe       # Rückseite
        self.aufgedeckt = False

    def aufdecken(self) -> None:
        self.aufgedeckt = True

    def zudecken(self) -> None:
        self.aufgedeckt = False

    def vergleichen(self, andere: Karte) -> bool:
        return self.symbol == andere.symbol

    def sichtbar(self) -> str:
        if self.aufgedeckt: return self.symbol
        return self.farbe



k1 = Karte("🐍", "🟦")







def spielfeld():
    karten = [k[k["sichtbar"]] for k in  kombis]
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
        karte = {}
        karte["vorne"] = vorne
        karte["hinten"] = hinten
        karte["sichtbar"] = "hinten"

        kombis.append(karte)

random.shuffle(kombis)

while any(k["sichtbar"] == "hinten" for k in kombis):
    spielfeld()
    try:
        i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
    except ValueError as e:
        print("Bitte zwei Zahlen eingeben.", e)
        continue

    # if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j:
    #     print("Ungültige Indizes.")
    #     continue

    if kombis[i]["sichtbar"] == "vorne" or kombis[j]["sichtbar"] == "vorne":
        print("Diese Karte ist schon aufgedeckt.")
        continue

    kombis[i]["sichtbar"] = "vorne"
    kombis[j]["sichtbar"] = "vorne"

    spielfeld()


    if kombis[i].vergleichen(kombis[j]):
        print("Paar gefunden!")

    else:
        print("Kein Paar.")
        kombis[i]["sichtbar"] = "hinten"
        kombis[j]["sichtbar"] = "hinten"

print("Glückwunsch! Du hast alle Paare gefunden.")
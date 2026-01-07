import random


class Card:
    def __init__(self, vorne: str, hinten: str):
        self.vorne = vorne
        self.hinten = hinten
        self.sichtbar = "hinten"  # entweder "hinten" oder "vorne"

    def zeige_symbol(self) -> str:
        # Was soll auf dem Spielfeld angezeigt werden?
        return self.vorne if self.sichtbar == "vorne" else self.hinten

    def ist_vorne(self) -> bool:
        return self.sichtbar == "vorne"

    def aufdecken(self) -> None:
        self.sichtbar = "vorne"

    def zudecken(self) -> None:
        self.sichtbar = "hinten"


def spielfeld(karten_liste: list[Card]) -> None:
    karten = [k.zeige_symbol() for k in karten_liste]
    print("Karten: ", *karten)
    print("Index:  ", end=" ")
    for i in range(len(karten)):
        print(f"{i:2}", end=" ")
    print("\n")


# --- Setup (wie vorher, nur mit Card-Objekten) ---

karte_vorne = ("🐍", "🐢", "🐸")
karte_hinten = ("🟦", "🟥")

kombis: list[Card] = []
for hinten in karte_hinten:
    for vorne in karte_vorne:
        kombis.append(Card(vorne=vorne, hinten=hinten))

random.shuffle(kombis)

# --- Spielschleife (Logik bleibt sehr ähnlich) ---

while any(not k.ist_vorne() for k in kombis):
    spielfeld(kombis)
    try:
        i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
    except ValueError as e:
        print("Bitte zwei Zahlen eingeben.", e)
        continue

    # Minimal sinnvolle Validierung (sonst knallt es bei falschen Indizes)
    if i < 0 or i >= len(kombis) or j < 0 or j >= len(kombis) or i == j:
        print("Ungültige Indizes.")
        continue

    if kombis[i].ist_vorne() or kombis[j].ist_vorne():
        print("Diese Karte ist schon aufgedeckt.")
        continue

    kombis[i].aufdecken()
    kombis[j].aufdecken()

    spielfeld(kombis)

    if kombis[i].vorne == kombis[j].vorne:
        print("Paar gefunden!")
    else:
        print("Kein Paar.")
        kombis[i].zudecken()
        kombis[j].zudecken()

print("Glückwunsch! Du hast alle Paare gefunden.")

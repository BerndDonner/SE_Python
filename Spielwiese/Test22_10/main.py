import random

Karten_pool = (
    "🐶", "🐱", "🐭", "🐹", "🐰",
    "🦊", "🐻", "🐼", "🐨", "🐯",
    "🦁", "🐮", "🐷", "🐸", "🐵",
    "🐔", "🐧", "🐦", "🐤", "🐺",
)

level = input("Mit wievielen Kartenpaaren willst Du spielen? ")

Karten_alle = list(Karten_pool)
random.shuffle(Karten_alle)
Karten_alle = Karten_alle[:int(level)]

Karte_verdeckt = "🎴"

Karten_deck = Karten_alle*2
random.shuffle(Karten_deck)

Zahlen = [ f"{i+1:2}" for i in range(len(Karten_deck))]
Karten_sichtbar = [Karte_verdeckt]*len(Karten_deck)

print(Karten_deck)


while Karte_verdeckt in Karten_sichtbar:
    print(Karten_sichtbar)
    print(Zahlen)

    auswahl = input("Welche Karten soll ich aufdecken? ")
    karte1, karte2 = auswahl.split()
    i1, i2 = int(karte1)-1, int(karte2)-1

    if Karten_sichtbar[i1] != Karte_verdeckt or Karten_sichtbar[i2] != Karte_verdeckt:
        print("❌ Zwei verdeckte Karten wählen!")
        continue        

    #Karten aufdecken
    Karten_sichtbar[i1] = Karten_deck[i1]
    Karten_sichtbar[i2] = Karten_deck[i2]

    print(Karten_sichtbar)

    if Karten_sichtbar[i1] != Karten_sichtbar[i2]:
        print("❌ Das war wohl nix!")
        Karten_sichtbar[i1] = Karte_verdeckt
        Karten_sichtbar[i2] = Karte_verdeckt
    else:
        print("✔️ Wow, du bist ein echte Pro!")


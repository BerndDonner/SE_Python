import random


Karten_symbole = "🐍  🐢  🐸  🦋 🎮 🔥 ✨ 🎯 🚀 👾 🐶 🐱 🐭 🐹 🐰 🦊 🍎 🍐 🍊 🍋 🍌 🍉 ⭐ 🌙 ☀️ ⚡ 🌈 ❄️"
Karte_verdeckt = "🎴"  # Blumenspielkarte als verdeckte Karte

Kartendeck = Karten_symbole.split()
Karten = Kartendeck

random.shuffle(Karten)

FrageAnzahl= input("\nMit wie vielen Kartenpaaren möchten Sie spielen? ") 
FrageAnzahl= int(FrageAnzahl)
Karten = Karten[:FrageAnzahl]*2

print("\n Mit diesen " ,FrageAnzahl, " Kartenpaaren spielen Sie jetzt Memory!\n", " ".join(Karten[:FrageAnzahl]))
random.shuffle(Karten)

Sichtbar = [Karte_verdeckt] * len(Karten)

def Spielfeld():
      print("\nKartennummer: ", " ".join(f"{i+1:02}" for i in range(len(Karten))))
      print("Karten:       ", " ".join(Sichtbar))
      print()
Spielfeld()

while Karte_verdeckt in Sichtbar:
    auswahl = input("Welche zwei Karten möchten Sie aufdecken? ")
    karte1, karte2 = auswahl.split()
    print(f"Sie haben die Karten {karte1} und {karte2} gewählt.")

    i1, i2 = int(karte1)-1, int(karte2)-1

    Sichtbar[i1], Sichtbar[i2] = Karten[i1], Karten[i2]
    Spielfeld()

    if Karten[i1] == Karten[i2]:
        print("✅ Paar gefunden!")
    else:
        print("❌ Kein Paar.")
        Sichtbar[i1], Sichtbar[i2] = Karte_verdeckt, Karte_verdeckt
        Spielfeld()
print("Glückwunsch! Sie haben alle Paare gefunden.")

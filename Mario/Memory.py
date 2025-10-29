Karten_alle = ["🦄 🐶 🐱 🐸 🦊 🐵 🐧 🐢 🐙 🦋"]
Karte_verdeckt = "🎴"
print(Karten_alle)
Splitted = Karten_alle[0].split()
input("Drücke Enter um das Spiel zu starten...")
Kartenzahl = input("Wie viele Paare möchtest du spielen? (Maximal 10 Paare) ")
Splitted = Splitted[0:int(Kartenzahl)]
print(Splitted)
Karten = Splitted * 2
print(Karten)
import random
random.shuffle(Karten)
print(Karten)
Zahlen = [ f"{i+1:02}" for i in range(len(Karten))]
Karten_verdeckt = [Karte_verdeckt]*len(Karten)
print(Zahlen)
print(Karten_verdeckt)
# ============================================
def zeige_spielfeld():
    print("\nIndex : ", " ".join(Zahlen))
    print("Karten: ", " ".join(Karten_verdeckt))
    print()
zeige_spielfeld()

while Karte_verdeckt in Karten_verdeckt:    
    auswahl = input("Welche Karten möchtest du aufdecken?")
    Karte1, Karte2 = auswahl.split()
    print(f"Du hast die Karten {Karte1} und {Karte2} gewählt.")
    i1, i2 = int(Karte1)-1, int(Karte2)-1
    # ============Karten aufdecken================
    Karten_verdeckt[i1]=Karten[i1]
    Karten_verdeckt[i2]=Karten[i2]
    print(Karten_verdeckt)
    if Karten[i1]==Karten[i2]:
        print("✅ Paar gefunden!")
    else:
        print("❌ Kein Paar.")
        Karten_verdeckt[i1]=Karte_verdeckt
        Karten_verdeckt[i2]=Karte_verdeckt 
    print(Karten_verdeckt)
# ============================================



# Karte_unsichtbar = "??"
# Karten_sichtbar = [Karte_unsichtbar] * len(Karten)
# print(Karten_sichtbar)
# while Karte_unsichtbar in Karten_sichtbar:
#     try:
#         i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
#         if i == j or not (0 <= i < len(Karten)) or not (0 <= j < len(Karten)):
#             print("❌ Ungültige Eingabe.")
#             continue
#         if Karten_sichtbar[i] != Karte_unsichtbar or Karten_sichtbar[j] != Karte_unsichtbar:
#             print("❌ Diese Karte ist schon aufgedeckt.")
#             continue
#         links, rechts = min(i, j), max(i, j)
#         print("Ausschnitt der Karten (Slice):", " ".join(Karten[links:rechts+1]))
#         Karten_sichtbar[i], Karten_sichtbar[j] = Karten[i], Karten[j]
#         zeige_spielfeld()
#         if Karten[i] == Karten[j]:
#             print("✅ Paar gefunden!")
#         else:
#             print("❌ Kein Paar.")
#             Karten_sichtbar[i], Karten_sichtbar[j] = Karte_unsichtbar, Karte_unsichtbar
#     except ValueError:
#         print("Bitte zwei Zahlen eingeben.")
#         continue
# print("🎉 Alle Paare gefunden! Spiel beendet.")
# ============================================

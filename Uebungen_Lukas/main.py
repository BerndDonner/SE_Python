import random

# 🧩 Aufgabe 1 – Kartenpool erweitern
# 20 verschiedene Karten-Emojis
# Tuple wird hier verwendet, weil es unveränderlich ist (immutable)
# Vorteil: Schutz vor unbeabsichtigtem Ändern des Kartenpools
Karten_alle = (
    "🍎", "⚽", "🚗", "🌻", "🐠", "🎲", "🍩", "🐱", "🌈", "🚀",
    "🍕", "🎧", "🐸", "🌵", "🦋", "🎁", "🍪", "🐢", "🍇", "🧩"
)

Karte_verdeckt = "🎴"
# 🧩 Aufgabe 2 – Schwierigkeitsstufe
while True:
    try:
        paare = int(input(f"Wie viele Kartenpaare möchtest du spielen? (1–{len(Karten_alle)}): "))
        if 1 <= paare <= len(Karten_alle):
            break
        else:
            print("Bitte eine Zahl im gültigen Bereich eingeben!")
    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl eingeben!")

# Teilmenge auswählen (z. B. 5 Paare)
auswahl_karten = list(Karten_alle[:paare])  # slicing: wähle Teilmenge
Karten_deck = auswahl_karten * 2  # doppelt (für Paare)

# Unterschied zwischen direkter und kopierter Liste
alle = list(Karten_alle)
b = alle  # verweist auf dasselbe Objekt
random.shuffle(b)
print("\n🔀 Nach shuffle(b) mit direkter Referenz:")
print("b =", b)
print("alle =", alle)

alle = list(Karten_alle)
b = alle[:]  # Kopie der Liste
random.shuffle(b)
print("\n🔀 Nach shuffle(b) mit Kopie (alle[:]):")
print("b =", b)
print("alle =", alle)

# Karten mischen
random.shuffle(Karten_deck)

# Zeige Karten einmal an (zum Einprägen)
print("\n🃏 Diese Karten sind im Spiel:")
print(" ".join(Karten_deck))
input("Drücke Enter, um das Spiel zu starten...")

# Spielfeld vorbereiten
Zahlen = [f"{i+1:2}" for i in range(len(Karten_deck))]
Karten_sichtbar = [Karte_verdeckt] * len(Karten_deck)

# Spiel-Loop
while Karte_verdeckt in Karten_sichtbar:
    print("\nAktuelles Spielfeld:")
    print(" ".join(Karten_sichtbar))
    print(" ".join(Zahlen))

    auswahl = input("Welche zwei Karten möchtest du aufdecken? (z. B. '3 7') → ")
    try:
        karte1, karte2 = auswahl.split()
        i1, i2 = int(karte1) - 1, int(karte2) - 1

        if i1 == i2 or not (0 <= i1 < len(Karten_deck)) or not (0 <= i2 < len(Karten_deck)):
            print("❗ Ungültige Auswahl, bitte andere Zahlen wählen.")
            continue

        # Karten aufdecken
        Karten_sichtbar[i1] = Karten_deck[i1]
        Karten_sichtbar[i2] = Karten_deck[i2]
        print(" ".join(Karten_sichtbar))

        if Karten_deck[i1] == Karten_deck[i2]:
            print("✔️ Super, ein Paar gefunden!")
        else:
            print("❌ Leider kein Paar.")
            Karten_sichtbar[i1] = Karte_verdeckt
            Karten_sichtbar[i2] = Karte_verdeckt

    except ValueError:
        print("❗ Bitte zwei Zahlen mit Leerzeichen eingeben.")

print("🎉 Glückwunsch! Du hast alle Paare gefunden!")
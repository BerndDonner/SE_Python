# ============================================
# 🧠 MEMORY in der Konsole
# Thema: Listen, Indizes, Slices
# Eingabe der Emojies mit Windows-Taste + .
# oder                    Windows-Taste + ;
# ============================================

import random

# --- Vorbereitung: Karten mischen ---
karten_pool = ("🐍", "🐢", "🐸", "🦋", "🐰", "🦊", "🐻", "🐯")
karte_unsichtbar = ("🟦", "🟥")

karten = []

# --- Karten erzeugen ---
for symbol in karten_pool:
    for farbe in karte_unsichtbar:
        karte = {
            "vorne": symbol,
            "hinten": farbe,
            "x": 0,
            "y": 0,
            "sichtbar": False,
            "index": None
        }
        karten.append(karte)


random.shuffle(karten)
for i, karte in enumerate(karten):
    karte["index"] = i


# Hilfsfunktion zum Anzeigen des Spielfelds
def zeige_spielfeld():
    print("\nIndex : ", " ".join(f"{karte["index"]:02}" for karte in karten))
    print("Karten: ", " ".join(
        karte["vorne"] if karte["sichtbar"] else karte["hinten"]
        for karte in karten))
    print()

# --- Spielschleife ---
while not all(k["sichtbar"] for k in karten):
    zeige_spielfeld()
    try:
        # Eingabe
        i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
        if i == j or not (0 <= i < len(karten)) or not (0 <= j < len(karten)):
            print("❌ Ungültige Eingabe.")
            continue
        if karten[i]["sichtbar"] or karten[j]["sichtbar"]:
            print("❌ Diese Karte ist schon aufgedeckt.")
            continue

        # Karten aufdecken
        karten[i]["sichtbar"] = True
        karten[j]["sichtbar"] = True
        zeige_spielfeld()

        # Vergleich
        if karten[i]["vorne"] == karten[j]["vorne"]:
            print("✅ Paar gefunden!")
        else:
            print("❌ Kein Paar.")
            karten[i]["sichtbar"] = False
            karten[j]["sichtbar"] = False

    except ValueError:
        print("Bitte zwei Zahlen eingeben.")
        continue

print("🎉 Alle Paare gefunden! Spiel beendet.")


# ============================================
# 🧠 MEMORY in der Konsole
# Thema: Listen, Indizes, Slices
# Eingabe der Emojies mit Windows-Taste + .
# oder                    Windows-Taste + ;
# ============================================

import random

# --- Vorbereitung: Karten mischen ---
karten = ["🐍", "🐍", "🐢", "🐢", "🐸", "🐸", "🦋", "🦋", "🐰", "🐰", "🦊", "🦊", "🐻", "🐻", "🐯", "🐯"]
karte_unsichtbar = "??"
random.shuffle(karten)

# verdeckte Karten: Liste aus Fragezeichen
sichtbar = [karte_unsichtbar] * len(karten)

# Hilfsfunktion zum Anzeigen des Spielfelds
def zeige_spielfeld():
    print("\nIndex : ", " ".join(f"{i:02}" for i in range(len(karten))))
    print("Karten: ", " ".join(sichtbar))
    print()

# --- Spielschleife ---
while karte_unsichtbar in sichtbar:
    zeige_spielfeld()
    try:
        # Spieler wählt zwei Karten
        i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())

        # Eingaben prüfen
        if i == j or not (0 <= i < len(karten)) or not (0 <= j < len(karten)):
            print("❌ Ungültige Eingabe.")
            continue
        if sichtbar[i] != karte_unsichtbar or sichtbar[j] != karte_unsichtbar:
            print("❌ Diese Karte ist schon aufgedeckt.")
            continue

        # --- Slice-Demo ---
        # Zeige einen Ausschnitt der echten Kartenliste
        links, rechts = min(i, j), max(i, j)
        print("Ausschnitt der Karten (Slice):", " ".join(karten[links:rechts+1]))

        # Aufdecken
        sichtbar[i], sichtbar[j] = karten[i], karten[j]
        zeige_spielfeld()

        # Vergleich
        if karten[i] == karten[j]:
            print("✅ Paar gefunden!")
        else:
            print("❌ Kein Paar.")
            sichtbar[i], sichtbar[j] = karte_unsichtbar, karte_unsichtbar

    except ValueError:
        print("Bitte zwei Zahlen eingeben.")
        continue

print("🎉 Alle Paare gefunden! Spiel beendet.")


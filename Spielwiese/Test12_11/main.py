# ============================================
# 🧠 MEMORY in der Konsole (mit zip)
# Thema: Listen, Indizes, Slices
# Eingabe der Emojis mit Windows-Taste + . oder ;
# ============================================

import random

# --- Vorbereitung: Karten mischen ---
karten_pool = ("🐍", "🐢", "🐸", "🦋", "🐰", "🦊", "🐻", "🐯")
l = 3

karte_vorne = random.sample(karten_pool, l)
karte_hinten = ("🟦", "🟥")

kombis = [(hinten, vorne) for hinten in karte_hinten for vorne in karte_vorne]
random.shuffle(kombis)

# Hilfsfunktion zum Anzeigen des Spielfelds
def zeige_spielfeld():
    sichtbar = [s for s, _ in kombis]
    print("Karten:  ", " ".join(sichtbar))
    print("Index : ", " ".join(f"{i:2}" for i in range(1, len(kombis)+1)))
    print()

# --- Spielschleife ---
while not all(sichtbar in karte_vorne for sichtbar, _ in kombis):
    zeige_spielfeld()
    try:
        i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 0 1)? ").split())
        i -= 1
        j -= 1

        if i == j or not (0 <= i < len(kombis)) or not (0 <= j < len(kombis)):
            print("❌ Ungültige Eingabe.")
            continue
        if kombis[i][0] in karte_vorne or kombis[j][0] in karte_vorne:
            print("❌ Diese Karte ist schon aufgedeckt.")
            continue

        # Karten aufdecken
        a, b = kombis[i]
        kombis[i] = (b, a)

        a, b = kombis[j]
        kombis[j] = (b, a)
        
        zeige_spielfeld()

        # Vergleich
        if kombis[i][0] == kombis[j][0]:
            print("✅ Paar gefunden!")
        else:
            print("❌ Kein Paar.")
            a, b = kombis[i]
            kombis[i] = (b, a)

            a, b = kombis[j]
            kombis[j] = (b, a)

    except ValueError:
        print("Bitte zwei Zahlen eingeben.")
        continue

print("🎉 Alle Paare gefunden! Spiel beendet.")





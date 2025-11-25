# ============================================
# 🧠 MEMORY in der Konsole (mit dict)
# Thema: Listen, Indizes, Slices, Dictionaries
# Tipp: Emojis unter Windows mit Windows-Taste + . oder ;
# ============================================

import random

# --- Vorbereitung: Karten mischen ---
# Mögliche Symbole für die Vorderseiten
karten_pool = ("🐍", "🐢", "🐸", "🦋", "🐰", "🦊", "🐻", "🐯")
anzahl_paare = 3  # Anzahl verschiedener Paare (Motiv-Paare)

# Zufällige Auswahl von Vorderseiten
karte_vorne = random.sample(karten_pool, anzahl_paare)

# Rückseiten-Varianten (jede Vorderseite kommt mit beiden Rückseiten vor)
karte_hinten = ("🟦", "🟥")

# Liste von Karten als Dictionaries:
# - "vorne": Motiv
# - "hinten": Rückseite
# - "sichtbar": aktuell angezeigte Seite ("vorne" oder "hinten")
kombis = [
    {"hinten": hinten, "vorne": vorne, "sichtbar": "hinten"}
    for hinten in karte_hinten
    for vorne in karte_vorne
]

# Karten zufällig anordnen
random.shuffle(kombis)

# --- Hilfsfunktion zum Anzeigen des Spielfelds ---
def zeige_spielfeld():
    # Für jede Karte die Seite anzeigen, die im Feld "sichtbar" steht
    sichtbar = [karte[karte["sichtbar"]] for karte in kombis]
    print("Karten: ", " ".join(sichtbar))
    # Indizes 1-basiert anzeigen (für die Eingabe durch den Spieler)
    print("Index : ", " ".join(f"{i:2}" for i in range(1, len(kombis) + 1)))
    print()

# --- Spielschleife ---
# Läuft, bis alle Karten aufgedeckt sind ("sichtbar" == "vorne")
while any(karte["sichtbar"] == "hinten" for karte in kombis):
    zeige_spielfeld()
    try:
        # Eingabe: zwei Kartenpositionen, z. B. "1 2"
        i, j = map(int, input("Welche zwei Karten möchten Sie aufdecken (z. B. 1 2)? ").split())
        # Umwandlung von 1-basiert (Anzeige/Eingabe) zu 0-basiert (Listen-Index)
        i -= 1
        j -= 1

        # Ungültige Eingaben abfangen
        if i == j or not (0 <= i < len(kombis)) or not (0 <= j < len(kombis)):
            print("❌ Ungültige Eingabe.")
            continue
        if kombis[i]["sichtbar"] == "vorne" or kombis[j]["sichtbar"] == "vorne":
            print("❌ Diese Karte ist schon aufgedeckt.")
            continue

        # --- Karten aufdecken ---
        kombis[i]["sichtbar"] = "vorne"
        kombis[j]["sichtbar"] = "vorne"
        
        zeige_spielfeld()

        # --- Vergleich: Paar gefunden? ---
        if kombis[i]["vorne"] == kombis[j]["vorne"]:
            print("✅ Paar gefunden!")
        else:
            print("❌ Kein Paar.")
            # Karten wieder umdrehen
            kombis[i]["sichtbar"] = "hinten"
            kombis[j]["sichtbar"] = "hinten"

    except ValueError:
        print("Bitte zwei Zahlen eingeben.")
        continue

print("🎉 Alle Paare gefunden! Spiel beendet.")

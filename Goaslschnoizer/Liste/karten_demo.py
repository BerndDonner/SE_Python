# Demo: Karten-Emojis für Memory-Spiel

# Verschiedene Möglichkeiten für verdeckte Karten:
karte_verdeckt = {
    "rechteck": "⬛",         # Schwarzes Rechteck
    "quadrat": "◼️",         # Schwarzes Quadrat
    "karte": "🎴",           # Blumenspielkarte
    "joker": "🃏",           # Joker-Karte
    "dunkel": "▪️",          # Schwarzes kleines Quadrat
    "abstrakt": "❇️",        # Funkeln
}

# Beispiel für Kartenpärchen (können als aufgedeckte Karten verwendet werden):
karten_paare = [
    "🐶", "🐱", "🐭", "🐹", "🐰", "🦊",  # Tiere
    "🍎", "🍐", "🍊", "🍋", "🍌", "🍉",  # Früchte
    "⭐", "🌙", "☀️", "⚡", "🌈", "❄️",  # Natur
]

print("Mögliche verdeckte Karten:")
for name, symbol in karte_verdeckt.items():
    print(f"{symbol} : {name}")

print("\nBeispiel für ein 4x4 Spielfeld mit verdeckten Karten:")
spielfeld = [[karte_verdeckt["karte"]] * 4 for _ in range(4)]

for reihe in spielfeld:
    print(" ".join(reihe))

print("\nBeispiel für aufgedeckte Karten (Paare):")
# Zeige die ersten 8 Paare in einem 4x4 Raster
for i in range(0, 4):
    print(" ".join(karten_paare[i:i+4]))

print("\nSimulation einer Spielsituation:")
spielfeld[1][1] = karten_paare[0]  # Erste Karte aufgedeckt
spielfeld[2][2] = karten_paare[0]  # Zweites Paar gefunden

print("\nSpielfeld mit zwei aufgedeckten Karten:")
for reihe in spielfeld:
    print(" ".join(reihe))
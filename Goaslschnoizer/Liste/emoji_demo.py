# Demo: Emojis in Python
# Es gibt mehrere Möglichkeiten, Emojis in Python zu verwenden:

# 1. Direkt als Unicode-Zeichen einfügen
print("Direkte Emojis: 👋 🐍 🎮 👾")

# 2. Unicode-Codepoints verwenden
print("Unicode Codepoints:", "\U0001F44D")  # 👍 Daumen hoch

# 3. Unicode-Namen verwenden
print("Unicode Namen:", "\N{GRINNING FACE}")  # 😀

# 4. Unicode-Escapesequenzen
print("Escapesequenz:", "\u263A")  # ☺

# Liste einiger häufig verwendeter Emojis mit Erklärung
emojis = {
    "👍": "Daumen hoch",
    "😊": "Lächelndes Gesicht",
    "🐍": "Python-Schlange",
    "❤️": "Rotes Herz",
    "🎮": "Gamepad",
    "🔥": "Feuer",
    "✨": "Funkeln",
    "🎯": "Zielscheibe",
    "🚀": "Rakete",
    "💡": "Glühbirne"
}

# Alle Emojis mit ihrer Bedeutung ausgeben
print("\nEmoji-Liste mit Bedeutung:")
for emoji, bedeutung in emojis.items():
    print(f"{emoji} : {bedeutung}")

# Praktisches Beispiel: Emoji-basiertes Feedback
punktzahl = 85
if punktzahl >= 90:
    feedback = "🏆"  # Trophäe
elif punktzahl >= 80:
    feedback = "⭐"  # Stern
elif punktzahl >= 70:
    feedback = "👍"  # Daumen hoch
else:
    feedback = "💪"  # Bizeps (weitermachen!)

print(f"\nDeine Punktzahl: {punktzahl} {feedback}")

# Tipp: Um alle verfügbaren Unicode-Namen zu sehen:
# import unicodedata
# unicodedata.name('😀')  # Gibt 'GRINNING FACE' zurück
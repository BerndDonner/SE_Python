import pygame
import random
import sys

# --- Setup ---
pygame.init()
pygame.display.set_caption("🧠 Memory – Pygame Edition")

#5+5+5+5=20 10Kartenpaare
#4+5+5+4=18  9Kartenpaare
#4+4+4+4=16  8Kartenpaare
#3+4+4+3=14  7Kartenppare
#4+4+4  =12  6Kartenpaare
#3+4+3  =10  5Kartenpaare
#3+2+3  =8   4Kartenpaare
#3+3    =6   3Kartenpaare
#2+2    =4   2Kartenpaare


WIDTH, HEIGHT = 800, 600
CARD_W, CARD_H = 100, 140

patterns = {
    10: [5,5,5,5],
    9: [4,5,5,4],
    8: [4,4,4,4],
    7: [3,4,4,3],
    6: [4,4,4],
    5: [3,4,3],
    4: [3,2,3],
    3: [3,3],
    2: [2,2],
}

for pairs, pattern in patterns.items():
    pos = generate_positions(pattern, WIDTH, HEIGHT, CARD_W, CARD_H)
    print(f"{pairs} pairs ({len(pos)} cards): pattern={pattern}")
    print(pos[:5], "...")



FONT = pygame.font.SysFont("Segoe UI Emoji", 72)
SMALL = pygame.font.SysFont("Arial", 24)
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# --- Daten vorbereiten ---
karten_pool = ("S", "X", "I", "O", "A", "B", "E", "H")
rueckseiten = ("🟥", "🟦")

# Alle Karten erzeugen (jeweils einmal rot/blau)
karten = []
for symbol in karten_pool:
    for farbe in rueckseiten:
        karten.append({
            "vorne": symbol,
            "hinten": farbe,
            "sichtbar": False,
        })

random.shuffle(karten)

# --- Spielfeld-Layout ---

# input Spielfeld WIDTH, HEIGHT
# make it simple create a fixed layout!!!

if floor(WIDTH/card_w) * floor(HEIGHT/card_h) >= len(karten): #kein Überlapp nötig
    scale = ...

    cols = floor(WIDTH/card_w)
    rows = floor(HEIGHT/card_h)

    
    

len(karten)
cols = 4
rows = len(karten) // cols
card_w, card_h = 150, 150
margin = 20
start_x = (WIDTH - (cols * (card_w + margin)) + margin) // 2
start_y = 60

# Positionen berechnen
for idx, karte in enumerate(karten):
    col = idx % cols
    row = idx // cols
    karte["rect"] = pygame.Rect(
        start_x + col * (card_w + margin),
        start_y + row * (card_h + margin),
        card_w,
        card_h
    )

# --- Spielstatus ---
erste_karte = None
zweite_karte = None
wartezeit = 0

# --- Hilfsfunktionen ---
def generate_positions(pattern, width, height, card_w, card_h):
    """
    pattern: list[int]  -> cards per row
    width, height: total area
    card_w, card_h: card size
    returns list[(x, y)]
    """
    positions = []

    rows = len(pattern)
    max_cols = max(pattern)

    # horizontal + vertical spacing
    total_w = width
    total_h = height
    h_space = (total_w - max_cols * card_w) / (max_cols + 1)
    v_space = (total_h - rows * card_h) / (rows + 1)

    y = v_space
    for row_cards in pattern:
        # center shorter rows horizontally
        row_width = row_cards * card_w + (row_cards + 1) * h_space
        offset_x = (total_w - row_width) / 2 + h_space

        x = offset_x
        for _ in range(row_cards):
            positions.append((x, y))
            x += card_w + h_space

        y += card_h + v_space

    return positions

def draw_text_center(surface, text, font, color, rect):
    img = font.render(text, True, color)
    r = img.get_rect(center=rect.center)
    surface.blit(img, r)

def zeichne_spielfeld():
    SCREEN.fill((40, 40, 50))
    for karte in karten:
        rect = karte["rect"]
        if karte["sichtbar"]:
            draw_text_center(SCREEN, karte["vorne"], FONT, (255, 255, 255), rect)
        else:
            draw_text_center(SCREEN, karte["hinten"], FONT, (200, 200, 200), rect)

    text = f"Gefundene Paare: {sum(k['sichtbar'] for k in karten) // 2}/{len(karten)//2}"
    label = SMALL.render(text, True, (255, 255, 255))
    SCREEN.blit(label, (20, 20))

    pygame.display.flip()

# --- Hauptschleife ---
running = True
while running:
    CLOCK.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and wartezeit == 0:
            pos = event.pos
            for karte in karten:
                if karte["rect"].collidepoint(pos) and not karte["sichtbar"]:
                    karte["sichtbar"] = True
                    if not erste_karte:
                        erste_karte = karte
                    elif not zweite_karte:
                        zweite_karte = karte

    # Wenn zwei Karten aufgedeckt sind
    if erste_karte and zweite_karte and wartezeit == 0:
        if erste_karte["vorne"] == zweite_karte["vorne"]:
            # ✅ Paar gefunden
            erste_karte = None
            zweite_karte = None
        else:
            # ❌ kurz warten, dann wieder umdrehen
            wartezeit = pygame.time.get_ticks() + 1000  # 1 Sekunde warten

    # Nach Ablauf der Wartezeit wieder umdrehen
    if wartezeit and pygame.time.get_ticks() >= wartezeit:
        erste_karte["sichtbar"] = False
        zweite_karte["sichtbar"] = False
        erste_karte = None
        zweite_karte = None
        wartezeit = 0

    zeichne_spielfeld()

    # Ende prüfen
    if all(k["sichtbar"] for k in karten):
        SCREEN.fill((30, 30, 40))
        win_text = SMALL.render("🎉 Alle Paare gefunden! Spiel beendet.", True, (255, 255, 255))
        SCREEN.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False


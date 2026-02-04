import os
import time
import random


def clear_screen() -> None:
    # Windows: cls, sonst: clear
    os.system("cls" if os.name == "nt" else "clear")


def pause(sec: float = 0.9) -> None:
    time.sleep(sec)


class Card:
    def __init__(self, name: str, stats: dict[str, int]) -> None:
        if not name or name.strip() == "":
            raise ValueError("name darf nicht leer sein")
        if not isinstance(stats, dict) or len(stats) == 0:
            raise ValueError("stats muss ein nicht-leeres dict sein")
        for k, v in stats.items():
            if not k or k.strip() == "":
                raise ValueError("Attributname darf nicht leer sein")
            if v < 0:
                raise ValueError("Werte müssen >= 0 sein")
        self.name = name
        self.stats = stats


class Player:
    def __init__(self, name: str, deck: list["Card"]) -> None:
        if not name or name.strip() == "":
            raise ValueError("Spielername darf nicht leer sein")
        self.name = name
        self.deck = deck

    def draw_top(self) -> "Card":
        if len(self.deck) == 0:
            raise RuntimeError("Deck ist leer")
        return self.deck.pop(0)

    def add_bottom(self, cards: list["Card"]) -> None:
        for c in cards:
            self.deck.append(c)


class Game:
    def __init__(self, p1: Player, p2: Player) -> None:
        self.p1 = p1
        self.p2 = p2
        self.pot: list[Card] = []
        self.current = 1  # 1 -> p1, 2 -> p2

    def runde(self, attr: str) -> str:
        if not attr or attr.strip() == "":
            raise ValueError("attr darf nicht leer sein")

        c1 = self.p1.draw_top()
        c2 = self.p2.draw_top()

        if attr not in c1.stats or attr not in c2.stats:
            raise KeyError("Attribut fehlt bei mindestens einer Karte")

        v1 = c1.stats[attr]
        v2 = c2.stats[attr]

        rep: list[str] = []
        rep.append(f"{self.p1.name} zieht {c1.name} ({attr}={v1})")
        rep.append(f"{self.p2.name} zieht {c2.name} ({attr}={v2})")

        if v1 > v2:
            rep.append(f"{self.p1.name} gewinnt")
            self.p1.add_bottom([c1, c2] + self.pot)
            self.pot = []
            self.current = 1
        elif v2 > v1:
            rep.append(f"{self.p2.name} gewinnt")
            self.p2.add_bottom([c1, c2] + self.pot)
            self.pot = []
            self.current = 2
        else:
            rep.append("Gleichstand -> Pott")
            self.pot.append(c1)
            self.pot.append(c2)
            # current bleibt gleich

        rep.append(f"Pottgröße: {len(self.pot)}")
        rep.append(f"Decks: {self.p1.name}={len(self.p1.deck)} | {self.p2.name}={len(self.p2.deck)}")
        return "\n".join(rep)


def spielen_quartett() -> None:
    cards = [
        Card("Auto A", {"speed": 120, "ps": 90, "weight": 1300}),
        Card("Auto B", {"speed": 130, "ps": 80, "weight": 1200}),
        Card("Auto C", {"speed": 125, "ps": 95, "weight": 1400}),
        Card("Auto D", {"speed": 110, "ps": 110, "weight": 1500}),
        Card("Auto E", {"speed": 140, "ps": 70, "weight": 1100}),
        Card("Auto F", {"speed": 115, "ps": 100, "weight": 1600}),
    ]

    rng = random.Random()
    rng.shuffle(cards)

    half = len(cards) // 2
    p1 = Player("A", cards[:half])
    p2 = Player("B", cards[half:])
    g = Game(p1, p2)

    while True:
        if len(p1.deck) == 0 or len(p2.deck) == 0:
            clear_screen()
            print("Spielende!")
            print(f"Decks: A={len(p1.deck)} | B={len(p2.deck)}")
            break

        clear_screen()
        current = p1 if g.current == 1 else p2
        print("Quartett")
        print(f"Am Zug: {current.name}")
        print(f"Decks: A={len(p1.deck)} | B={len(p2.deck)} | Pott={len(g.pot)}")
        print("Attribute: speed, ps, weight")
        attr = input("> ").strip()

        try:
            rep = g.runde(attr)
            print()
            print(rep)
            pause(1.2)
        except (ValueError, KeyError, RuntimeError) as e:
            print("Fehler:", e)
            pause(1.2)


def _tests_quartett() -> None:
    a = Card("A", {"x": 5})
    b = Card("B", {"x": 6})
    p1 = Player("P1", [a])
    p2 = Player("P2", [b])
    g = Game(p1, p2)
    rep = g.runde("x")
    assert "P2 gewinnt" in rep

    # Gleichstand + Pott
    a2 = Card("A2", {"x": 7})
    b2 = Card("B2", {"x": 7})
    p1 = Player("P1", [a2])
    p2 = Player("P2", [b2])
    g = Game(p1, p2)
    g.runde("x")
    assert len(g.pot) == 2

    # Fehlendes Attribut
    try:
        p1 = Player("P1", [Card("C", {"y": 1})])
        p2 = Player("P2", [Card("D", {"x": 1})])
        Game(p1, p2).runde("x")
        assert False
    except KeyError:
        pass


if __name__ == "__main__":
    _tests_quartett()
    spielen_quartett()
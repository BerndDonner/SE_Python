import random
import os
import time

class BattleshipBoard:
    def __init__(self) -> None:
        # Schiffe: Name -> Liste der Koordinaten (x, y)
        self.ships: dict[str, list[tuple[int, int]]] = {}
        # Schüsse: Koordinate -> "HIT" oder "MISS"
        self.shots: dict[tuple[int, int], str] = {}

    # ---------- Hilfsmethoden ----------
    def _check_pos(self, pos: tuple[int, int]) -> None:
        x, y = pos
        if not (0 <= x <= 5 and 0 <= y <= 5):
            raise ValueError("Koordinate außerhalb 0..5")

    def _delta(self, direction: str) -> tuple[int, int]:
        if direction == "N":
            return (0, -1)
        if direction == "E":
            return (1, 0)
        if direction == "S":
            return (0, 1)
        if direction == "W":
            return (-1, 0)
        raise ValueError("Direction muss N/E/S/W sein")

    def _occupied_dict(self) -> dict[tuple[int, int], bool]:
        occ: dict[tuple[int, int], bool] = {}
        for cells in self.ships.values():
            for c in cells:
                occ[c] = True
        return occ

    # ---------- Schiff platzieren ----------
    def place_ship(self, name: str, start: tuple[int, int], length: int, direction: str) -> None:
        if name in self.ships:
            raise RuntimeError("Schiffsname existiert bereits")
        if length <= 0:
            raise ValueError("Length muss > 0 sein")

        self._check_pos(start)
        dx, dy = self._delta(direction)

        coords: list[tuple[int, int]] = []
        x, y = start
        for _ in range(length):
            pos = (x, y)
            self._check_pos(pos)
            coords.append(pos)
            x += dx
            y += dy

        occ = self._occupied_dict()
        for c in coords:
            if c in occ:
                raise RuntimeError("Überlappung mit vorhandenem Schiff")

        self.ships[name] = coords
        assert len(self.ships[name]) == length, "Programmierfehler: falsche Schifflänge"

    def place_random(self, name: str, length: int, rng: random.Random) -> None:
        assert length <= 6, "Programmierfehler: length zu groß für 6x6"
        directions = ["N", "E", "S", "W"]
        while True:
            start = (rng.randint(0, 5), rng.randint(0, 5))
            direction = directions[rng.randint(0, 3)]
            try:
                self.place_ship(name, start, length, direction)
                return
            except (ValueError, RuntimeError):
                continue

    # ---------- Schuss abgeben ----------
    def shoot(self, pos: tuple[int, int]) -> str:
        self._check_pos(pos)
        if pos in self.shots:
            raise RuntimeError("Feld wurde bereits beschossen")

        hit = any(pos in cells for cells in self.ships.values())
        self.shots[pos] = "HIT" if hit else "MISS"
        return self.shots[pos]

    # ---------- Versenkte Schiffe ----------
    def sunk_ships(self) -> list[str]:
        res: list[str] = []
        for name, cells in self.ships.items():
            if all(self.shots.get(c) == "HIT" for c in cells):
                res.append(name)
        res.sort()
        return res

    def all_sunk(self) -> bool:
        if len(self.ships) == 0:
            return False
        return len(self.sunk_ships()) == len(self.ships)

    # ---------- Anzeige ----------
    def render(self, reveal_ships: bool) -> str:
        occ = self._occupied_dict() if reveal_ships else {}
        lines: list[str] = []
        for y in range(6):
            row: list[str] = []
            for x in range(6):
                p = (x, y)
                if p in self.shots:
                    row.append("x" if self.shots[p] == "HIT" else "o")
                elif reveal_ships and p in occ:
                    row.append("S")
                else:
                    row.append(".")
            lines.append(" ".join(row))
        return "\n".join(lines)

# ---------- Hilfsfunktionen ----------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause(seconds: float):
    time.sleep(seconds)

# ---------- Spiel starten ----------
def spielen_battleship() -> None:
    rng = random.Random()
    b = BattleshipBoard()
    b.place_random("A", 3, rng)
    b.place_random("B", 2, rng)
    b.place_random("C", 2, rng)

    schuesse_uebrig = 20
    while True:
        clear_screen()
        print("Schiffe versenken 6x6 (Eingabe: x y | q=quit)\n")
        print(b.render(reveal_ships=False))
        print(f"\nVersenkt: {b.sunk_ships()} | Schüsse übrig: {schuesse_uebrig}")

        if b.all_sunk():
            print("\nAlles versenkt! Glückwunsch!")
            break
        if schuesse_uebrig <= 0:
            print("\nKeine Schüsse mehr. Game Over.")
            print("\nLösung:\n" + b.render(reveal_ships=True))
            break

        cmd = input("> ").strip().lower()
        if cmd == "q":
            break
        try:
            x_str, y_str = cmd.split()
            x = int(x_str)
            y = int(y_str)
            res = b.shoot((x, y))
            print(res)
            schuesse_uebrig -= 1
            pause(0.8)
        except ValueError as e:
            print("Bitte zwei Zahlen eingeben (x y).", e)
            pause(1.1)
        except RuntimeError as e:
            print("Ungültiger Schuss:", e)
            pause(1.1)

# ---------- Test starten ----------
if __name__ == "__main__":
    spielen_battleship()
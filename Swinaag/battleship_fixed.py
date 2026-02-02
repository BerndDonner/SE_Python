import random

class BattleshipBoard:
    def __init__(self) -> None:
        # Initialize ships and shots as dictionaries
        self.ships: dict[str, list[tuple[int, int]]] = {}
        self.shots: dict[tuple[int, int], str] = {}
        # Initialize the board as a dictionary with (x, y) tuples as keys and "." as default values
        self.board: dict[tuple[int, int], str] = {(x, y): "." for x in range(6) for y in range(6)}

    def _check_pos(self, pos: tuple[int, int]) -> None:
        x, y = pos
        if x < 0 or x > 5 or y < 0 or y > 5:
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
        raise ValueError("direction muss N/E/S/W sein")

    def _occupied_dict(self) -> dict[tuple[int, int], bool]:
        occ: dict[tuple[int, int], bool] = {}
        for cells in self.ships.values():
            for c in cells:
                occ[c] = True
        return occ

    def place_ship(self, name: str, start: tuple[int, int], length: int, direction: str) -> None:
        if name in self.ships:
            raise RuntimeError("Schiffsname existiert bereits")
        if length <= 0:
            raise ValueError("length muss > 0 sein")

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
        assert len(self.ships[name]) == length, "Programmierfehler: falsche Schifflänge gespeichert"

    def place_random(self, name: str, length: int, rng: random.Random) -> None:
        # Contract: Für 6x6 sind Längen > 6 sinnlos
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

    def shoot(self, pos: tuple[int, int]) -> str:
        self._check_pos(pos)
        if pos in self.shots:
            raise RuntimeError("Feld wurde bereits beschossen")

        hit = False
        for cells in self.ships.values():
            if pos in cells:
                hit = True
                break

        self.shots[pos] = "HIT" if hit else "MISS"
        return self.shots[pos]

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
            lines.append("".join(row))
        return "\n".join(lines)


def spielen_battleship() -> None:
    rng = random.Random()
    b = BattleshipBoard()
    b.place_random("A", 3, rng)
    b.place_random("B", 2, rng)
    b.place_random("C", 2, rng)

    shots_left = 20
    while True:
        print("\033[H\033[J", end="")  # Clear screen
        print("Schiffe versenken 6x6 (Eingabe: x y | q=quit)")
        print()
        print(b.render(reveal_ships=False))
        print()
        print("Versenkt:", b.sunk_ships(), f"| Schüsse übrig: {shots_left}")

        if b.all_sunk():
            print("\nAlles versenkt! Glückwunsch!")
            break
        if shots_left <= 0:
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
            shots_left -= 1
        except ValueError as e:
            print("Bitte zwei Zahlen eingeben (x y).", e)
        except RuntimeError as e:
            print("Ungültiger Schuss:", e)

if __name__ == "__main__":
    spielen_battleship()
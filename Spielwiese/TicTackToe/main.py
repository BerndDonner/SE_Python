import os
import time
from typing import Optional


def clear_screen() -> None:
    # Windows: cls, sonst: clear
    os.system("cls" if os.name == "nt" else "clear")


def pause(sec: float = 0.9) -> None:
    time.sleep(sec)
    

class TicTacToe:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._board: list[str] = ["." for _ in range(9)]
        self._winner: Optional[str] = None
        self._history: list[int] = []  # pos-Liste für Undo

    def _pos(self, x: int, y: int) -> int:
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise ValueError("x,y müssen 0..2 sein")
        return y * 3 + x

    def render(self) -> str:
        b = self._board
        return (
            f"{b[0]} {b[1]} {b[2]}\n"
            f"{b[3]} {b[4]} {b[5]}\n"
            f"{b[6]} {b[7]} {b[8]}"
        )

    def ist_voll(self) -> bool:
        return "." not in self._board

    def gewinner(self) -> Optional[str]:
        if self._winner is not None:
            return self._winner

        b = self._board
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        ]
        for i, j, k in lines:
            if b[i] != "." and b[i] == b[j] == b[k]:
                self._winner = b[i]
                return self._winner
        return None

    def zug_xy(self, x: int, y: int, symbol: str) -> None:
        if symbol not in ("X", "O"):
            raise ValueError("symbol muss 'X' oder 'O' sein")
        if self.gewinner() is not None:
            raise RuntimeError("Spiel ist bereits beendet")

        pos = self._pos(x, y)
        if self._board[pos] != ".":
            raise RuntimeError("Feld ist bereits belegt")

        self._board[pos] = symbol
        self._history.append(pos)
        self.gewinner()

    def undo(self) -> None:
        if len(self._history) == 0:
            raise RuntimeError("Kein Zug zum Undo vorhanden")
        if self._winner is not None:
            # Undo muss Gewinner-Cache zurücksetzen, weil sich das Ergebnis ändern kann
            self._winner = None

        pos = self._history.pop()
        self._board[pos] = "."
        # Invariante: Board enthält nur X/O/.
        assert all(c in ("X", "O", ".") for c in self._board), "Programmierfehler: ungültiges Board-Zeichen"


def spielen_ttt() -> None:
    g = TicTacToe()
    current = "X"

    while True:
        clear_screen()
        print("TicTacToe (Eingabe: x y | u = undo | q = quit)")
        print()
        print(g.render())
        w = g.gewinner()
        if w is not None:
            print()
            print(f"{w} gewinnt!")
            break
        if g.ist_voll():
            print()
            print("Unentschieden!")
            break

        cmd = input(f"Spieler {current}> ").strip().lower()
        if cmd == "q":
            break
        if cmd == "u":
            try:
                g.undo()
                current = "O" if current == "X" else "X"
            except RuntimeError as e:
                print(e)
                pause(1.0)
            continue

        try:
            x_str, y_str = cmd.split()
            x = int(x_str)
            y = int(y_str)
            g.zug_xy(x, y, current)
            current = "O" if current == "X" else "X"
        except ValueError as e:
            print("Bitte zwei Zahlen eingeben (x y).", e)
            pause(1.1)
        except RuntimeError as e:
            print("Ungültiger Zug:", e)
            pause(1.1)


def _tests_ttt_engine() -> None:
    g = TicTacToe()
    g.zug_xy(0, 0, "X")
    g.zug_xy(1, 0, "O")
    g.zug_xy(1, 1, "X")
    g.zug_xy(2, 0, "O")
    g.zug_xy(2, 2, "X")
    assert g.gewinner() == "X", "X sollte gewinnen"

    try:
        g.zug_xy(0, 2, "O")
        assert False, "Zug nach Spielende sollte RuntimeError auslösen"
    except RuntimeError:
        pass

    g2 = TicTacToe()
    try:
        g2.zug_xy(0, 0, "A")
        assert False
    except ValueError:
        pass

    g3 = TicTacToe()
    g3.zug_xy(0, 0, "X")
    g3.undo()
    assert g3.gewinner() is None
    assert g3._board[0] == ".", "Undo sollte Feld leeren"


if __name__ == "__main__":
    _tests_ttt_engine()
    spielen_ttt()
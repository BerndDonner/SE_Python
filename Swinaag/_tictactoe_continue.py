# src/main.py

class TicTacToe:
    def __init__(self):
        self.board = ["."] * 9
        self.history = []

    def reset(self) -> None:
        self.board = ["."] * 9
        self.history = []

    def zug_xy(self, x: int, y: int, symbol: str) -> None:
        if not (0 <= x < 3 and 0 <= y < 3):
            raise ValueError("Ungültige Koordinaten")
        if symbol not in ["X", "O"]:
            raise ValueError("Ungültiges Symbol")
        index = x * 3 + y
        if self.board[index] != ".":
            raise RuntimeError("Feld belegt oder Zug nach Spielende")

        self.board[index] = symbol
        self.history.append((x, y))

    def gewinner(self):
        # Check rows, columns and diagonals for a winner
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)             # Diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != ".":
                return self.board[a]
        return None

    def ist_voll(self) -> bool:
        return all(cell != "." for cell in self.board)

    def render(self) -> str:
        return "\n".join([" | ".join(row) for row in [self.board[i:i+3] for i in range(0, 9, 3)]])
    



    # src/main.py

import os
import time

def spielen_ttt():
    game = TicTacToe()
    current_symbol = "X"
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(game.render())
        
        try:
            user_input = input("Geben Sie die Koordinaten ein (z.B. 1 2) oder 'u' für Undo: ")
            if user_input.lower() == "u":
                if game.history:
                    last_move = game.history.pop()
                    x, y = last_move
                    game.board[x * 3 + y] = "."
                else:
                    print("Kein Zug zum Undo!")
            else:
                x, y = map(int, user_input.split())
                game.zug_xy(x, y, current_symbol)
        except (ValueError, RuntimeError) as e:
            print(e)
            time.sleep(1)
        
        winner = game.gewinner()
        if winner:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(game.render())
            print(f"Der Gewinner ist {winner}!")
            break
        
        if game.ist_voll():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(game.render())
            print("Unentschieden!")
            break
        
        current_symbol = "O" if current_symbol == "X" else "X"

if __name__ == "__main__":
    spielen_ttt()



    # src/main.py

def test_tic_tac_toe():
    game = TicTacToe()
    
    # Test initial state
    assert all(cell == "." for cell in game.board)
    
    # Test zug_xy method
    game.zug_xy(0, 0, "X")
    assert game.board[0] == "X"
    
    # Test undo functionality
    game.zug_xy(1, 1, "O")
    game.history.pop()
    assert game.board[1*3 + 1] == "."
    
    # Test winner detection
    game.board = ["X", "X", "X", ".", ".", ".", ".", ".", "."]
    assert game.gewinner() == "X"
    
    # Test full board
    game.reset()
    for i in range(9):
        game.zug_xy(i // 3, i % 3, "O" if i % 2 else "X")
    assert game.ist_voll()

test_tic_tac_toe()
from encodings.cp856 import encoding_table
import os
import time
import random
from typing import Optional

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def pause(sec: float = 0.9) -> None:
    time.sleep(sec)




class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        print("Willkommen zu Tic Tac Toe!")
        pause(5.0)
        self.board: list[str] = ['.' for _ in range(9)]

    def zug_xy(self, x: int, y: int, symbol: str) -> None:
        if not (0 <= x <= 2 and 0 <= y <= 2):
            raise ValueError("x und y müssen zwischen 0 und 2 liegen.")
        if symbol not in ('X', 'O'):
            raise ValueError("Symbol muss entweder'X' oder 'O'.")
        index = y * 3 + x

        # Check if the game has already ended
        if self.gewinner() is not None:
            raise RuntimeError("Das Spiel ist bereits beendet.")
        
        # Check if the cell is already occupied
        if self.board[index] != '.':
            raise RuntimeError("Das Feld ist bereits belegt.")
        self.board[index] = symbol

    def gewinner(self) -> Optional[str]:
        # Define winning combinations (rows, columns, diagonals)
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]

        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] in ('X', 'O'):
                return self.board[a]  # Return the winner ('X' or 'O')

        return None  # No winner yet
    
    def ist_voll(self) -> bool:
        # Check if there are no empty cells ('.') on the board
        return '.' not in self.board
    
    def render(self) -> str:
        # Create a string representation of the board with coordinates
        rows = [f"{i} | " + " | ".join(self.board[i*3:(i+1)*3]) for i in range(3)]
        header = "    0   1   2"
        separator = "--+---+---+--"
        return f"{header}\n" + f"\n{separator}\n".join(rows)

def spielen_ttt():
    # Clear the screen at the start of the game
    clear_screen()
    # Initialize the game
    game = TicTacToe()
    current_symbol = 'X'  # Start with X

    # Track the last move
    last_move = None

    while True:
        clear_screen()
        
        print(game.render())

        # Check for a winner
        winner = game.gewinner()
        if winner:
            print(f"Spieler {winner} hat gewonnen!")
            play_again = input("Möchten Sie erneut spielen? (y/n): ").lower()
            if play_again == 'y':
                game.reset()
                current_symbol = 'X'  # Reset to starting player
                last_move = None
                continue
            else:
                print("Spiel beendet. Danke fürs Spielen!")
                break

        # Check if the board is full
        if game.ist_voll():
            print("Unentschieden! Das Spielfeld ist voll.")
            play_again = input("Möchten Sie erneut spielen? (y/n): ").lower()
            if play_again == 'y':
                game.reset()
                current_symbol = 'X'
                last_move = None
                continue
            else:
                print("Spiel beendet. Danke fürs Spielen!")
                break

        try:
            # Prompt the user for input
            user_input = input(f"Spieler {current_symbol}, geben Sie Ihre Koordinaten ein (x y) oder nehmen Sie Ihren letzten Zug zurück (u): ")

            if user_input.lower() == 'u':
                if last_move is None:
                    print("Kein Zug zum Rückgängig machen.")
                else:
                    x, y = last_move
                    game.board[y * 3 + x] = '.'  # Undo the last move
                    current_symbol= 'O' if current_symbol == 'X' else 'X'  # Switch back the symbol
                    last_move = None
                pause(5.0)
                continue

            x, y = map(int, user_input.split())
            game.zug_xy(x, y, current_symbol)
            last_move = (x, y)  # Store the last move

            # Switch the current symbol
            current_symbol = 'O' if current_symbol == 'X' else 'X'
        except ValueError:
            print("Ungültiges Format. Bitte geben Sie zwei Zahlen im Format 'x y' ein oder 'u' für Undo.")
            pause(5.0)
        except RuntimeError as e:
            print(e)
            pause(5.0)

if __name__ == "__main__":
    spielen_ttt()


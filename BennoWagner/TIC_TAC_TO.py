import random
import os
import string

class tictac:
    def __init__(self,index):
        self.index=index
        self.status = "."

    def X_treffer(self):
        self.status="X"

    def O_treffer(self):
        self.status="O"  

class Spielen:
    def __init__(self):
        self.grid_index= []
        for i in range(9):
            self.grid_index.append(tictac(i))

        self.render()    

        w=True


        while True:


            x_schuss, y_schuss = map(int, input("Gib X und Y ein (z.B. 0 1): ").split())
            if w==True and self.grid_index[y_schuss*3+x_schuss].status == ".":
                self.grid_index[y_schuss*3+x_schuss].X_treffer()
            elif self.grid_index[y_schuss*3+x_schuss].status == "O" or self.grid_index[y_schuss*3+x_schuss].status == "X":
                print("Du Schlingel das Feld ist schon besetzt")
                continue   
            elif w==False and self.grid_index[y_schuss*3+x_schuss].status == ".":
                self.grid_index[y_schuss*3+x_schuss].O_treffer()
            elif self.grid_index[y_schuss*3+x_schuss].status == "X" or self.grid_index[y_schuss*3+x_schuss].status == "O":
                print("Du Schlingel das Feld ist schon von X besetzt")
                continue    

            # Definiere alle Gewinnkombinationen
            winning_combinations = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Reihen
                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Spalten
                [0, 4, 8], [2, 4, 6]              # Diagonalen
            ]

            # Prüfe Gewinn
            for combo in winning_combinations:
                if all(self.grid_index[i].status == "X" for i in combo):
                    print("X hat GEWONNEN!!!")
                    break
                elif all(self.grid_index[i].status == "O" for i in combo):
                    print("O hat GEWONNEN!!!")
                    break




            self.render()
            w=not w


        
          
    def render (self):
        print("   " + " ".join(str(i) for i in range(3)))

        m=self.grid_index              

        for zeilen_index in range(3):
            zeile = []
            for spalten_index in range(3):
                index = zeilen_index * 3 + spalten_index
                zeile.append(m[index].status)
            print(f"{zeilen_index:2} " + " ".join(zeile))


spiel=Spielen()

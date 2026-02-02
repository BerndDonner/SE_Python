import random
import os
import string


class Battleship:
    def __init__(self, name, länge, x_position, y_position, orientierung):
        self.name = name
        self.länge = länge
        self.x_position = x_position
        self.y_position = y_position
        self.orientierung = orientierung
        self.infomation = []
        self.delta = (0,0)

        if self.orientierung == "N":
            self.delta = (0, 1)
        if self.orientierung == "O":
            self.delta = (1, 0)
        if self.orientierung == "S":
            self.delta = (0, -1)
        if self.orientierung == "W":
            self.delta = (-1, 0)

        x = self.x_position
        y = self.y_position
        dx, dy = self.delta
        self.infomation.append([self.name, x, y, "~"])
        for i in range(self.länge - 1):
            x = x + dx
            y = y + dy
            self.infomation.append([self.name, x, y, "~"])


    def print(self):
        print(self.infomation)

class Spiel_Funktion:
    def __init__(self):
        self.meer: list[str] = ["~" for i in range(36)]
        self.munition=20

        while True:
            j = 2
            self.Schiffe = []
            for i in ["A", "B", "C"]:
                L = j
                orientierung = random.choice(["N", "O", "S", "W"])
                if orientierung == "O":  # nach rechts
                    x = random.randint(0, 6 - L)
                    y = random.randint(0, 5)
                elif orientierung == "W":  # nach links
                    x = random.randint(L - 1, 5)
                    y = random.randint(0, 5)
                elif orientierung == "N":  # nach oben
                    x = random.randint(0, 5)
                    y = random.randint(0, 6 - L)
                elif orientierung == "S":  # nach unten
                    x = random.randint(0, 5)
                    y = random.randint(L - 1, 5)
                self.Schiffe.append(Battleship("i", L, x, y, orientierung))
                j = j + 1

            indexe = []
            for i in self.Schiffe:
                for feld in i.infomation:
                    if 0 <= feld[1] <= 5 and 0 <= feld[2] <= 5:
                        idx = feld[2] * 6 + feld[1]
                        indexe.append(idx)

            if len(indexe) == len(set(indexe)):
                break

        for i in self.Schiffe:
            for name, x, y, status in i.infomation:
                index = y * 6 + x
                self.meer[index] = status

        self.render()        

        while True:
            x_schuss, y_schuss = map(int, input("Gib X und Y ein (z.B. 1 3): ").split())
            os.system("clear")
            self.schießen(x_schuss,y_schuss)
            self.munition=self.munition-1
            if self.munition==0:
                print("VERLOREN! TRINK MAL EIN ZIELWASSER!")
                break
            elif self.meer.count("S") == 9:
                print("DU SCHWITZER! HASTE X-RAYS BENUTZT!")
                break
            self.render()
        

    def schießen(self, x_schuss, y_schuss):
        for i in self.Schiffe:
            # Treffer markieren
            for feld in i.infomation:
                if feld[1] == x_schuss and feld[2] == y_schuss and feld[3] == "~":
                    feld[3] = "H"
            # Prüfen, ob Schiff versenkt ist
            if all(f[3] == "H" for f in i.infomation):
                for f in i.infomation:
                    f[3] = "S"
        else:
            # Wenn kein Treffer auf irgendein Schiff
            self.meer[y_schuss*6 + x_schuss] = "0"

        # Spielfeld aktualisieren
        for i in self.Schiffe:
            for feld in i.infomation:
                self.meer[feld[2]*6 + feld[1]] = feld[3]


    def render(self):
        m = self.meer
        print("   " + " ".join(str(i) for i in range(6)))

        for zeilen_index in range(6):
            zeile = []
            for spalten_index in range(6):
                index = zeilen_index * 6 + spalten_index
                zeile.append(m[index])
            print(f"{zeilen_index:2} " + " ".join(zeile))
        print(f"Munition:{self.munition}")    

# Spiel starten und Schuss abgeben
spiel = Spiel_Funktion()


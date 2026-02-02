import string
import os
import random


class Gitter:
    def __init__(self, spalten: int, zeilen: int, anzahl_sachen: int, platzhalter: str = "."):
        # Prüfen, ob Eingaben gültig sind
        assert 1 <= spalten <= 26, "Spalten: 1–26 erlaubt"
        assert zeilen > 0, "Zeilen müssen > 0 sein"
        assert 0 <= anzahl_sachen <= spalten * zeilen, "Zu viele Sachen für das Gitter"

        # Eigenschaften speichern
        self.spalten = spalten
        self.zeilen = zeilen
        self.gesamt_felder = spalten * zeilen      # maximale Anzahl Felder
        self.anzahl_sachen = anzahl_sachen         # wie viele Sachen wirklich da sind
        self.platzhalter = platzhalter

        # Speicher für die Sachen
        self.daten = [platzhalter] * self.gesamt_felder

        # Spalten-Beschriftungen: A, B, C, ...
        self.spalten_beschriftung = string.ascii_uppercase[:spalten]

    # ---------- Anzeige ----------
    def anzeigen(self):
        # Terminal leeren
        os.system("cls" if os.name == "nt" else "clear")

        # Spaltenüberschrift
        print("   " + " ".join(self.spalten_beschriftung))

        # Jede Zeile durchgehen
        for zeilen_index in range(self.zeilen):
            zeile = []
            for spalten_index in range(self.spalten):
                index = zeilen_index * self.spalten + spalten_index  # 1D-Index berechnen
                # Zeige Sache, wenn vorhanden, sonst leer
                zeile.append(self.daten[index] if index < self.anzahl_sachen else " ")
            # Zeile mit Nummer ausgeben
            print(f"{zeilen_index:2} " + " ".join(zeile))

        # Legende
        print("\nLegende: '.' = Platzhalter, leer = freies Feld")
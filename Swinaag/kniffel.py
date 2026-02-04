import os
import time
import random


def clear_screen() -> None:
    # Windows: cls, sonst: clear
    os.system("cls" if os.name == "nt" else "clear")


def pause(sec: float = 0.9) -> None:
    time.sleep(sec)


def _validate_wurf(w: list[int]) -> None:
    if len(w) != 5:
        raise ValueError("Wurf muss Länge 5 haben")
    for x in w:
        if x < 1 or x > 6:
            raise ValueError("Würfelwerte müssen 1..6 sein")


def roll(n: int, rng: random.Random) -> list[int]:
    if n <= 0:
        raise ValueError("n muss > 0 sein")
    return [rng.randint(1, 6) for _ in range(n)]


def reroll(w: list[int], indices: list[int], rng: random.Random) -> None:
    _validate_wurf(w)
    for idx in indices:
        if idx < 0 or idx > 4:
            raise ValueError("indices nur 0..4")
    for idx in indices:
        w[idx] = rng.randint(1, 6)


def count_faces(w: list[int]) -> dict[int, int]:
    _validate_wurf(w)
    d: dict[int, int] = {i: 0 for i in range(1, 7)}
    for x in w:
        d[x] += 1
    return d


def summe(w: list[int]) -> int:
    _validate_wurf(w)
    return sum(w)


def dreierpasch(w: list[int]) -> int:
    d = count_faces(w)
    return summe(w) if max(d.values()) >= 3 else 0


def viererpasch(w: list[int]) -> int:
    d = count_faces(w)
    return summe(w) if max(d.values()) >= 4 else 0


def kniffel(w: list[int]) -> int:
    d = count_faces(w)
    return 50 if max(d.values()) == 5 else 0


def full_house(w: list[int]) -> int:
    d = count_faces(w)
    vals = sorted(d.values(), reverse=True)
    return 25 if (3 in vals and 2 in vals) else 0


def kleine_strasse(w: list[int]) -> int:
    _validate_wurf(w)
    s = set(w)  # rein algorithmisch, aber set wurde noch nicht behandelt -> Alternative unten
    # Wenn du wirklich strikt ohne set willst, kann man das per list-Check lösen.
    patterns = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
    for p in patterns:
        if p.issubset(s):
            return 30
    return 0


def grosse_strasse(w: list[int]) -> int:
    _validate_wurf(w)
    s = set(w)
    return 40 if (s == {1, 2, 3, 4, 5} or s == {2, 3, 4, 5, 6}) else 0


CATS: list[str] = ["3P", "4P", "FH", "KS", "GS", "K"]


def score(cat: str, w: list[int]) -> int:
    if cat == "3P":
        return dreierpasch(w)
    if cat == "4P":
        return viererpasch(w)
    if cat == "FH":
        return full_house(w)
    if cat == "KS":
        return kleine_strasse(w)
    if cat == "GS":
        return grosse_strasse(w)
    if cat == "K":
        return kniffel(w)
    raise ValueError("Unbekannte Kategorie")


def beste_kategorie(w: list[int]) -> tuple[str, int]:
    assert len(CATS) > 0, "Programmierfehler: CATS darf nicht leer sein"
    best_cat = ""
    best_pts = -1
    for cat in sorted(CATS):
        pts = score(cat, w)
        if pts > best_pts:
            best_pts = pts
            best_cat = cat
    assert best_cat != "", "Programmierfehler: best_cat wurde nicht gesetzt"
    return (best_cat, best_pts)


def spielen_kniffel_eine_runde() -> None:
    rng = random.Random()
    w = roll(5, rng)

    rerolls_left = 2
    while True:
        clear_screen()
        print("Kniffel (eine Runde)")
        print("Wurf:", w)
        print(f"Neu würfeln übrig: {rerolls_left}")
        print("Eingabe: reroll i j k  |  ok  |  q")
        cmd = input("> ").strip().lower()

        if cmd == "q":
            return
        if cmd == "ok":
            break
        if cmd.startswith("reroll"):
            if rerolls_left <= 0:
                print("Keine Neu-Würfe mehr.")
                pause(1.0)
                continue
            parts = cmd.split()
            try:
                indices = [int(x) for x in parts[1:]]
                reroll(w, indices, rng)
                rerolls_left -= 1
            except ValueError as e:
                print("Ungültige Eingabe:", e)
                pause(1.1)
        else:
            print("Unbekanntes Kommando.")
            pause(1.0)

    cat, pts = beste_kategorie(w)
    print(f"\nBeste Kategorie: {cat} = {pts} Punkte")
    pause(2.0)


def _tests_kniffel() -> None:
    assert full_house([2, 2, 3, 3, 3]) == 25
    assert full_house([2, 2, 2, 2, 3]) == 0
    assert kniffel([6, 6, 6, 6, 6]) == 50
    assert grosse_strasse([2, 3, 4, 5, 6]) == 40
    assert kleine_strasse([1, 2, 2, 3, 4]) == 30

    try:
        dreierpasch([1, 2, 3])
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    _tests_kniffel()
    spielen_kniffel_eine_runde()
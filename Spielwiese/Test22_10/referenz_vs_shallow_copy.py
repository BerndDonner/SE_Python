import random

# Ausgangsliste
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Original Liste a:      {a}")
# --------------------------------------------
# 🧩 Variante 1: Kopie durch Slice ([:] erzeugt flache Kopie)
# --------------------------------------------
b = a[:]              # b ist eine flache Kopie von a (neue Liste, gleiche Werte)
random.shuffle(b)     # nur b wird gemischt

# a bleibt unverändert
print(f"a nach shallow copy:   {a}")


# --------------------------------------------
# 🧩 Variante 2: Nur Referenzkopie (beide Namen zeigen auf dasselbe Objekt)
# --------------------------------------------
b = a                 # b und a verweisen jetzt auf dieselbe Liste im Speicher
random.shuffle(b)     # das Mischen ändert das gemeinsame Objekt

# a ist ebenfalls gemischt, da a und b identisch sind
print(f"a nach reference copy: {a}")

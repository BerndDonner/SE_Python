a = ["Benno", "Anian", "Lukas", "Thomas", "Antonia", "Andy", "Laurin\n", "Boomer", "Andy"]

# Iteration über die Liste mit einer for-each Schleife (Pythonic)
for name in a:
    print(name)

# Iteration über die Liste mit einer for-Schleife (C/Java-Style)
for i in range(len(a)):
    print(a[i])

del a[6]
a.remove("Andy")
a.remove("Andy")

print(a)


# Dies ist mein erstes python programm

a = 1
print(a)
print(type(a))

pi = 3.1415
print(pi)
print(type(pi))

b = 'Brutus: "Sag pi =', pi, 'oder stirb!"'
print(b)


# print(string, float, string)
print('Brutus: "Sag pi =', pi, 'oder stirb!"')
print('Brutus: "Sag pi = ' + str(pi) + ' oder stirb!"')

c = f'Brutus: "Sag pi = {pi} oder stirb!"'
print(c)

# erstelle ein kleine python programm dass eine schöne ASCII Tabbelle von A-Z bzw a-z erstellt
print("ASCII-Tabelle für a-z:")
for c in range(ord('a'), ord('z') + 1):
    print(f"{chr(c)} -> {c}")

print("\nASCII-Tabelle für A-Z:")
for c in range(ord('A'), ord('Z') + 1):
    print(f"{chr(c)} -> {c}")

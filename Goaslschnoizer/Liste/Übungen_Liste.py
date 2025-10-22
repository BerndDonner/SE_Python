#Liste
goaslschnoizer = ['Benno','Anian','Lukas','Thomas','Antonia','Andi','Laurin\n','Boomer']

#print Liste
print(goaslschnoizer)

#Liste in einzelnen Zeilen ausgeben
for namen in goaslschnoizer:
    print(namen)

#Liste mit Index ausgeben
for i in range(2,len(goaslschnoizer)):
    print(f"{i+1}. {goaslschnoizer[i]}")

#Liste erweitern
goaslschnoizer.append('Sepp')
print(goaslschnoizer)

#Liste an bestimmter Stelle erweitern
goaslschnoizer.insert(3,'Loisl')
print(goaslschnoizer)

#Liste entfernen
goaslschnoizer.remove('Sepp')
del goaslschnoizer[3]
print(goaslschnoizer)
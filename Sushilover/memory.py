import random #Bibliothek einfügen

#Variablen zuweisen
punkte = 0
versuche = 0
anzahl = 0
auswahl = [""]

#Spieler nach Kartenanzahl fragen
print("Wie viele Paare magst du haben? Wähle zwischen 2-20")
anzahl = int(input("Paaranzahl: "))

#Karten erzeugen, mischen und anzeigen
cards_autumn = ("🍂", "🍁", "🌰", "🎃", "🦔", "🌾", "☕", "🍎", "🥧", "🍄", "🧣", "🧤", "🪵", "🔥", "🌻", "🐿️", "🌽", "🌧️", "🕯️", "🍵")
cards_christmas = ("🎄", "🎅", "🤶", "🦌", "🛷", "❄️", "⛄", "🎁", "🕯️", "🔔","🍪", "🥛", "🍭", "🧦", "🧣", "🕯️", "🌟", "🍷", "🪵", "🎶")
selected_cards = random.sample(cards_autumn, anzahl) #random.sample wählt zufällig aus Tupel aus, anzahl sagt wie viele
memorycards = list(selected_cards)
test = memorycards
print(test)
test = memorycards[:]
print(test)
memorycards = memorycards * 2
random.shuffle(memorycards)
print("Das sind jetzt deine Karten: ", selected_cards)

#Zahlen und Speicherlisten erzeugen
mystery_cards = [f"{i+1:2}" for i in range(len(memorycards))]
save_cards = [f"{i+1:2}" for i in range(len(memorycards))]
#Spielstart
#print(memorycards)
print(mystery_cards)

while (punkte<anzahl):
    wahl1 = int(input("First card ")) #Eingabe der 1. Karte
    listnumber1 = wahl1 -1
    mystery_cards[listnumber1] = memorycards[listnumber1] #Übernahme der Eingabe und Anzeige
    print(mystery_cards)
    wahl2 = int(input("Second Card ")) #Eingabe 2. Karte
    listnumber2 = wahl2 -1
    mystery_cards[listnumber2] = memorycards[listnumber2] #Übernahme der Eingabe und Anzeige
    print(mystery_cards)
    versuche +=1 #Versuchszählung

    #Karten vergleichen
    if memorycards[listnumber1] == memorycards[listnumber2]: #Karten gleich
         
        punkte +=1
        print("Yes! Du hast", punkte, "Punkte!")

    else: #Karten ungleich
        
        mystery_cards[listnumber1] = save_cards[listnumber1]
        mystery_cards[listnumber2] = save_cards[listnumber2]
        print("No, try again!")
        


    print(mystery_cards) #Finalle Ausgabe

print("You win! With ", versuche, "trys!") #Ende des Spiels

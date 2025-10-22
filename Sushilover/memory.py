import random #Bibliothek einfügen

#Variablen zuweisen
punkte = 0
versuche = 0

#Karten erzeugen und mischen
cards_all = "🍂 🎃 🦔 🌻 ☕ 🔥 🍎 🍄"
memorycards = cards_all.split()
memorycards = memorycards * 2
random.shuffle(memorycards)

#Zahlen und Speicherlisten erzeugen
mystery_cards = [f"{i+1:2}" for i in range(len(memorycards))]
save_cards = [f"{i+1:2}" for i in range(len(memorycards))]
#Spielstart
#print(memorycards)
print(mystery_cards)

while (punkte<((len(cards_all)+1)/2)):
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

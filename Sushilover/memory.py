import random

punkte = 0
versuche = 0

cards_all = "🌻 🌼 🌸 🌹 🍀"
memorycards = cards_all.split()
memorycards = memorycards * 2
random.shuffle(memorycards)

mystery_cards = [f"{i+1:2}" for i in range(len(memorycards))]
save_cards = [f"{i+1:2}" for i in range(len(memorycards))]

print(memorycards)
print(mystery_cards)
while (punkte<((len(cards_all)+1)/2)):
    wahl1 = int(input("First card "))
    listnumber1 = wahl1 -1
    mystery_cards[listnumber1] = memorycards[listnumber1]
    print(mystery_cards)
    wahl2 = int(input("Second Card "))
    listnumber2 = wahl2 -1
    mystery_cards[listnumber2] = memorycards[listnumber2]
    print(mystery_cards)
    versuche +=1
    if memorycards[listnumber1] == memorycards[listnumber2]:
         
        punkte +=1
        print("Yes! Du hast", punkte, "Punkte!")

    else:
        
        mystery_cards[listnumber1] = save_cards[listnumber1]
        mystery_cards[listnumber2] = save_cards[listnumber2]
        print("No, try again!")
        


    print(mystery_cards)

print("You win! With ", versuche, "trys!")

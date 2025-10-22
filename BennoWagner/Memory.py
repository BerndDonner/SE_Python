import random

counter_richtig = 0
counter_falsch = 0
memory_liste="\U0001F600 \U0001F602 \U0001F680 \U0001F40D \U0001F916"
memory_liste_copy=memory_liste.split()
memory_liste_copy=memory_liste_copy*2
memory_liste_ausgabe = [f"{'\U0001F0A0':2}" for _ in range(len(memory_liste_copy))]
Zahlen = [ f"{i+1:2}" for i in range (len(memory_liste_copy))]

random.shuffle(memory_liste_copy)

print(memory_liste_copy)
print(Zahlen)
print(memory_liste_ausgabe)
print("Merke dir die Zuording!")


taste = input("Drücke 'E' und Enter, um weiterzumachen: ")

if taste.lower() == 'e':
    print("\n" * 10)
    print(memory_liste_ausgabe)
    print(Zahlen)

    for versuch in range(1, 11):
      print("\n" * 3)
      print("    ")
      Auswahl = input("Welche Karten soll ich aufdecken? ")
      karte1,karte2=Auswahl.split()
      i1,i2=memory_liste_copy[int(karte1)-1],memory_liste_copy[int(karte2)-1]

      if(i1==i2):
        print("Richtig")
        memory_liste_ausgabe[int(karte1)-1],memory_liste_ausgabe[int(karte2)-1]=i1,i1  
        print(memory_liste_ausgabe)
        print(Zahlen)
        print("")

      else:
         print("falsch")
         print(memory_liste_ausgabe)
         print(Zahlen)
         print("    ")
   
        
      if f"{'\U0001F0A0':2}" not in memory_liste_ausgabe:
           print("Gewonnen!")
           break
      
      if(versuch>=10):
         print("Verloren")   
  
    

else:
    print("Du hast nicht 'E' gedrückt.")




















import random

counter_richtig =0
counter_falsch = 0
memory_kartenpool=("🐶", "🐱", "🦊", "🐻", "🐼",
    "🐨", "🐯", "🦁", "🐸", "🐵",
    "🐧", "🐦", "🦆", "🐤", "🦉",
    "🐺", "🦄", "🐝", "🐞", "🦂")

kartenbereich = int(input("Gib mir eine Zahl zwischen 2 und 20 für das Memory-Spiel: "))

if 2 <= kartenbereich <= 20:

  memory_liste_copy=list(memory_kartenpool)[:kartenbereich]
  memory_liste_copy=memory_liste_copy*2
  memory_liste_ausgabe =["🟦"]*kartenbereich+["🟥"]*kartenbereich
  

  kombiniert_memory=list(zip(memory_liste_copy,memory_liste_ausgabe))
  random.shuffle(kombiniert_memory)
  memory_liste_copy, memory_liste_ausgabe = zip(*kombiniert_memory)
  memory_liste_ausgabe=list(memory_liste_ausgabe)
  memory_liste_copy=list(memory_liste_copy)



  Zahlen = [ f"{i+1:2}" for i in range (len(memory_liste_copy))]

  

  print(memory_liste_copy)
  print(memory_liste_ausgabe)
  print(Zahlen)
  print("Merke dir die Zuording!")


  taste = input("Drücke 'E' und Enter, um weiterzumachen: ")

  if taste.lower() == 'e':
      print("\n" * 10)
      print("----" * 30)
      print(f"{memory_liste_ausgabe}\tCounter Richtig:{counter_richtig} Counter Falsch:{counter_falsch}")
      print(Zahlen)

      for versuch in range(1, 11):
        print("\n" * 4)
        Auswahl = input("Welche Karten soll ich aufdecken? ")
        print("----" * 30)
        karte1,karte2=Auswahl.split()
        i1,i2=memory_liste_copy[int(karte1)-1],memory_liste_copy[int(karte2)-1]

        if(i1==i2):
          print("Richtig")
          counter_richtig=counter_richtig+1
          print(type(memory_liste_ausgabe))
          memory_liste_ausgabe[int(karte1)-1],memory_liste_ausgabe[int(karte2)-1]=i1,i1  
          print("")

        else:
          print("falsch")
          counter_falsch=counter_falsch+1
          print("    ")

        print(f"{memory_liste_ausgabe}\tCounter Richtig:{counter_richtig} Counter Falsch:{counter_falsch}")
        print(Zahlen) 
        
    
          
        if f"🟦" not in memory_liste_ausgabe:
            print("Gewonnen!")
            break
        
        if(versuch>=10):
          print("Verloren")   
    
      

  else:
      print("Du hast nicht 'E' gedrückt.")

else:
  print("Die Zahl ist nicht GERADE oder nicht im Bereich von 2 bis 20.")


















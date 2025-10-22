import random

joa = ("🍂", "🍁", "🌰", "🎃", "🦔", "🌾", "☕", "🍎")
memorycards = list(joa)

test = memorycards[:]
random.shuffle(test)
print(memorycards)

test = memorycards
random.shuffle(test)
print(memorycards)


#b = alle
#random.shuffle(b)
#print(alle)
#b = alle[:]
#random.shuffle(b)
#print(alle)
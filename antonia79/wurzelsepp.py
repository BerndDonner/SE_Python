import struct

print("Hallo Wurzel Sepp!!")

print(4 * 3**2) # Potenz vor Multiplikation auch in Python


# Liebe Schüler und Schülerinnen,
# hier ist der Code für die schnelle Berechnung der Quadratwurzel
# Quake 3's Q_rsqrt
# https://en.wikipedia.org/wiki/Fast_inverse_square_root
# https://en.wikipedia.org/wiki/Fast_inverse_square_root#Algorithm
#
# Dieser Code ist complett von der Tabby KI generiert worden. Ist aber leider falsch :( (<---- Einzige Ausnahme diese Zeile)

def inv_sqrt(x):
    xhalf = 0.5 * x
    i = int.from_bytes(x.to_bytes(8, 'little'), 'little')  # treat float's bytes as int
    i = 0x5fe6eb50c7b537a9 - (i >> 1)  # initial guess for Newton's method
    x = float.fromhex(hex(i))  # treat int's bytes as float
    x = x * (1.5 - xhalf * x * x)  # One round of Newton's method
    return x

def inv_sqrt_gpt(x):
    """Schnelle Näherung für 1/sqrt(x) – inspiriert von Quake III Arena"""
    threehalfs = 1.5

    x2 = x * 0.5
    y = x

    # float → int (Bitmuster beibehalten)
    i = struct.unpack('Q', struct.pack('d', y))[0]

    # magische Konstante für double precision (64 Bit)
    i = 0x5fe6eb50c7b537a9 - (i >> 1)

    # int → float (Bitmuster beibehalten)
    y = struct.unpack('d', struct.pack('Q', i))[0]

    # Eine Iteration Newton-Verfahren
    y = y * (threehalfs - (x2 * y * y))
    return y


print(inv_sqrt_gpt(4))  # Should be close to 0.5
print(inv_sqrt_gpt(9))  # Should be close to 0.3333 
print(inv_sqrt_gpt(16)) # Should be close to 0.25
print(inv_sqrt_gpt(25)) # Should be close to 0.2

"""
print(10 ? 10)   #  = 100
print(9 ? 1)     #  = 8
print(121 ? 3)   #  = 40.333
print(2 ? 5)     #  = 32
print(17 ? 15)   #  = 2
print(56 ? 13)   #  = 4
print(8 ? 8)     #  = 16
"""

# Multiplication
if (10 * 10) == 100:
    print("True; multiplication; 10 * 10 = 100")
else:    
    print("False; multiplication; 10 * 10 != 100")

# Subtraction
if (9 - 1) == 8:
    print("True; subtraction; 9 - 1 = 8")
else:    
    print("False; subtraction; 9 - 1 != 8")

# Division
# division = 121/3
# (round(division, 3))
if (round(121 / 3, 3)) == 40.333:
    print("True; division; 121/3 = 40.333")
else:    
    print("False; division; 121/3 != 40.333")

# Exponentiation
if (2 ** 5) == 32:
    print("True; exponentiation; 2 ** 5 = 32")
else:    
    print("False; exponentiation; 2 ** 5 != 32")

# Modulo and subtraction
if (17 % 15) == 2 and (17 - 15) == 2:
    print("True; modulo and subtraction; 17 % 15 = 2 and 17 - 15 = 2")
else:    
    print("False; modulo and subtraction; 17 % 15 != 2 or 17 - 15 != 2")

# Modulo operation and Integer division
if (56 % 13) == 4 and (56 // 13) == 4:
    print("True; modulo and Integer division; 56 % 13 = 4 and (56 // 13) == 4")
else:    
    print("False; modulo and Integer division; 56 % 13 != 4 or (56 // 13) != 4")

# Addition
if (8 + 8) == 16:
    print("True; addition; 8 + 8 = 16")
else:    
    print("False; addition; 8 + 8 != 16")

# Vyzkoušej si hru FizzBuzz

# 1. Vytvoř proměnnou cislo, kam budeš ukládat vstup uživatele jako celé číslo,
cislo = int(input("Zadejte libovolné celé číslo: "))

# 2. Pokud je číslo dělitelné třemi, program by měl vypsat "Fizz".
if cislo % 3 == 0:
    print("Číslo je dělitelné 3.")
    print("Fizz")

# 3. Pokud je číslo dělitelné pěti, program by měl vypsat "Buzz".
if cislo % 5 == 0:
    print("Číslo je dělitelné 5.")
    print("Buzz")

# 4. Pokud je číslo dělitelné třemi i pěti, program by měl vypsat "FizzBuzz".
if cislo % 5 == 0 and cislo % 3 == 0:
    print("Číslo je dělitelné 3 i 5.")
    print("FizzBuzz")

# 5. Pokud číslo není dělitelné ani třemi, ani pěti, program by měl vypsat toto číslo.
if cislo % 5 != 0 and cislo % 3 != 0:
    print("Číslo není dělitelné 3 ani 5.")
    print(cislo)

# Asi hezčí/lepší? varianta>
'''
cislo = int(input("Zadejte celé číslo: "))

if cislo % 3 == 0 and cislo % 5 == 0:
    print("FizzBuzz")
elif cislo % 3 == 0:
    print("Fizz")
elif cislo % 5 == 0:
    print("Buzz")
else:
    print(cislo)
'''
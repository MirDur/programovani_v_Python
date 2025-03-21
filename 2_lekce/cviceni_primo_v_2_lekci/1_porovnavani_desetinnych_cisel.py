# cvičení "Vyzkoušej si porovnávání desetinných čísel"

# 1. Vytvoř proměnné cislo_1 a cislo_2, kam budeš ukládat vstup uživatele jako desetinná čísla.
cislo_1 = float(input("Zadejte první desetinné číslo: "))
cislo_2 = float(input("Zadejte druhé desetinné číslo: "))

'''
# 2. Pokud je hodnota v proměnné cislo_1 větší než cislo_2, program by měl vypsat "První číslo je větší než druhé.".
if cislo_1 > cislo_2:
    print("První číslo je větší než druhé.")

# 3. Pokud je hodnota v proměnné cislo_1 menší než cislo_2, program by měl vypsat "První číslo je menší než druhé.".
if cislo_1 < cislo_2:
        print("První číslo je menší než druhé.")

# 4. Pokud jsou obě hodnoty stejné, vypiš "Obě čísla jsou stejná.".
if cislo_1 == cislo_2:
        print("Obě čísla jsou stejná.")
'''

# Jeden if blok:
if cislo_1 == cislo_2:      print("Obě čísla jsou stejná.")
elif cislo_1 > cislo_2:     print("První číslo je větší než druhé.")
else:       print("První číslo je menší než druhé.")

# Možná hezčí varianta>
'''
if cislo_1 == cislo_2:
    print("Obě čísla jsou stejná.")
else:
    if cislo_1 < cislo_2:
        print("První číslo je menší než druhé.")
    else:
       print("První číslo je větší než druhé.")
'''
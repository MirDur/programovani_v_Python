'''
Sudá vs. lichá
V této úloze vytvoř program, který sečte odděleně všechna sudá a všechna lichá čísla ze seznamu.
Na konci by měl program vypsat absolutní hodnotu rozdílu mezi těmito součty.
Tvým ukolem je zjistit, jak iterovat každým prvkem v seznamu čísel, ne psát součet manuálně.
cisla = [1, 2, 3, 4, 5, 6, 7, 8]
Jednotlivé kroky, které program musí obsahovat:
'''

# 1. Zapiš hodnoty do proměnné uvedené výš.
cisla = [1, 2, 3, 4, 5, 6, 7, 8]

# 2. Sečti všechna sudá čísla a výsledek ulož do proměnné suda.
suda = 0
for cislo in cisla:
    if cislo % 2 == 0:
        suda = suda + cislo
print(suda)

# list comprehension

# 3. Sečti všechna lichá čísla a výsledek ulož do proměnné licha.

licha = 0
for cislo in cisla:
    if cislo % 2 != 0:
        licha = licha + cislo
print(licha)

# list comprehension

# 4. Nakonec získáš rozdíl mezi těmito dvěma součty (proměnná vysledek).
'''
for cislo in cisla:
    if cislo % 2 == 0:
        suda = suda + cislo
    else:
        licha = licha + cislo        
'''

vysledek = suda - licha
print("Rozdíl je: ", abs(vysledek))
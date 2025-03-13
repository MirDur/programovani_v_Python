'''
Dělitel
V této úloze vytvoř program, který potřebuje od uživatele start, stop a delitel.
Po zapracování vypíše všechna celá čísla v intervalu od start, do stop, která jsou dělitelná 
hodnotou v delitel.

vysledek = list()
start = 3
stop = 9
delitel = 3

Jednotlivé kroky, které program musí obsahovat:
'''

# 1. Zapiš hodnoty do proměnné uvedené výš.
vysledek = list()

start = 3

stop = 9
if start >= stop:
    print("Hodnota pro 'stop' musí být větší než hodnota pro 'start'")

delitel = 3
if delitel == 0:
    print("Zadejte prosím celé číslo různé od nuly.")

# 2. Ověř, jestli jsou proměnné start, stop a delitel datový typ int (pomocí built-in funkce isinstance).

# print("Je hodnota proměnné 'start' dat. typu 'int'?", isinstance(start, int))
# start = input("Zadejte prosím celočíselnou hodnotu 'start' (a potvrďte klávesou Enter): ")
# funkce input() převadí zadanou hodnotu na string
# stop = int(input("Zadejte prosím celočíselnou hodnotu 'stop' (a potvrďte klávesou Enter): "))
# print("Je hodnota proměnné 'stop' dat. typu 'int'?", isinstance(stop, int))
# delitel = int(input("Zadejte prosím celočíselnou hodnotu 'delitel' (a potvrďte klávesou Enter): "))
# print("Je hodnota proměnné 'delitel' dat. typu 'int'?", isinstance(delitel, int))
# Engeto nechce v rámci této úlohy přijímat hodnoty oživatele.

if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int):
    print("Hodnoty zadané pro 'start', 'stop' a 'delitel' jsou z oboru celých čísel.")

# 3. Pokud jsou int, vypiš oznámení dle ukázky níž.
'''
if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int):
    print("Zadaný rozsah: <", start, ",", stop, ">", sep="")
    for number in range(start, stop + 1):
        if number % delitel == 0:
            vysledek.append(number)
    print("Čísla dělitelná ", delitel, ": ", vysledek, sep="")
'''

# 4. Pokud alespoň jeden (vstup od uživatele) není int, vypiš oznámení dle ukázky níž a ukonči skript.
if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int):
    print("Zadaný rozsah: <", start, ",", stop, ">", sep="")
    for number in range(start, stop + 1):
        if number % delitel == 0:
            vysledek.append(number)
    print("Čísla dělitelná ", delitel, ": ", vysledek, sep="")
else:
    print("Zadané hodnoty musí být čísla z oboru celých čísel.")
    # import sys
    print("Skript bude nyní ukončen.")
    exit()  # Nebo quit()

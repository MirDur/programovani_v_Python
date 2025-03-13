'''
Délka slov, comprehensions
Pomocí slovníkové komprehence spočítej délky slov v zadané sekvenci.
Skript bude obsahovat:
'''

# 1. Zadanou proměnnou seznam_slov, s hodnotami: ["jablko", "pomeranč", "banán", "kiwi", "hruška"].

seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]

#for slovo in seznam_slov:
#        print(len(slovo), end=", ")

# 2. do proměnné delky_slov zapiš slovníkovou komprehenci tak, aby ukládála hodnoty ve formátu: slovo: delka_slova, tedy:"svetr": 5.

'''
delky_slov = dict()
for slovo in seznam_slov:
    delky_slov[slovo] = len(slovo)
'''

# Dict comprehension>
delky_slov = {slovo: len(slovo) for slovo in seznam_slov}

# 3. Nakonec vypiš výsledek (tzn. slovník seznam_slov) pomocí funkce print().
print(delky_slov)
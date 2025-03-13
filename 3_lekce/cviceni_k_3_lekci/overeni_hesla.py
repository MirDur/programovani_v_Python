'''
Ověření hesla
V této úloze vytvoř program, který se pokusí ověřit, jestli heslo vložené uživatelem patří k jeho účtu.
Jednotlivé kroky, které program musí obsahovat:
jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}
'''

# 1. Zapiš všechny proměnné výše.
jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}

# 2. Zapiš podmínku, která zkontroluje, jestli se hodnoty v proměnných jmeno a heslo shodují s klíčem a hodnotou ve slovníku uzivatel.
if jmeno in uzivatel and heslo == uzivatel[jmeno]:
# 3. Pokud se shodují, vypiš oznámení jako v ukázce níže.
# Ahoj Marek vítej v aplikaci! Pokračuj...
    print("Ahoj Marek vítej v aplikaci! Pokračuj...")
# 4. Pokud se neshodují, opět vypiš oznámení jako v ukázce níže.
# Uživatelské jméno nebo heslo nejsou v pořádku!
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")

'''
if 'Marek' in uzivatel:
    print("'Marek' is a key in 'uzivatel' dict.")

if '1234' in uzivatel:
    print("'1234' is a key in 'uzivatel' dict.")

# To <in> v if podmínce výše testuje přítomnost hodnoty před <in> ve slovníku "uzivatel"  .

uzivatel_keys = uzivatel.keys()
print(uzivatel_keys)
print(type(uzivatel_keys))

uzivatel_values = uzivatel.values()
print(uzivatel_values)
print(type(uzivatel_values))

uzivatel_items = uzivatel.items()
print(uzivatel_items)
print(type(uzivatel_items))
'''

'''
Řešení podle Engeto>

# Ověř jestli zadané jméno a heslo souhlasí s uloženými údaji ve sl. "uzivatel"
if uzivatel.get(jmeno) == heslo:
    # ... pokud SOUHLASÍ, přivítej uživatele jménem
    print("Ahoj", jmeno, "vítej v aplikaci! Pokračuj...")

else:
    # ... pokud NESOUHLASÍ, upozorni uživatele o omylu
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")

'''
# Vyzkoušej si metody pro list

# 1. Z proměnné zaznam, získej jednotlivé hodnoty rozdělené na řádcích, vyselektuj jen validní hodnoty.
zaznam = ['2021-01-01 11:11:11:1111 - něco se děje,',
'2021-01-01 11:12:11:1111 - nic to nebylo,',
'2021-01-01 11:13:11:1111 - a přece něco!,']
# Validní hodnota je co?!

print()
zaznam_1 = zaznam[0]
print("1. položka (řádek) seznamu 'zaznam'>", zaznam_1, sep="\n")
print("'Validní' část 1. položky>", zaznam_1[0:24], sep="\n", end="\n\n")

zaznam_2 = zaznam[1]
print("2. položka (řádek) seznamu 'zaznam'>", zaznam_2, sep="\n")
print("'Validní' část 2. položky>", zaznam_2[0:24], sep="\n", end="\n\n")

zaznam_3 = zaznam[2]
print("3. položka (řádek) seznamu 'zaznam'>", zaznam_3, sep="\n")
print("'Validní' část 3. položky>", zaznam_3[0:24], sep="\n", end="\n\n")


# 2. Na nultý index přidej hodnotu:
'''
addition = ['2021-01-01 11:10:11:1111 - BANG,\n',
'2021-01-01 11:11:11:1111 - něco se děje,',
'2021-01-01 11:12:11:1111 - nic to nebylo,',
'2021-01-01 11:13:11:1111 - a přece něco!,']
print("Položka (seznam), kterou budu chtít vložit do seznamu 'zaznam'>", addition, sep="\n", end="\n\n")

# zaznam_extended = [zaznam.insert(0, addition)]    # Vracelo [None]; metoda list.insert() upravuje seznam (list), na který je použita - nevrací v return vakue nový (a upravený) seznam.
zaznam.insert(0, addition)
print("(Původní) seznam 'zaznam' upravený o seznam 'additon' na index 0>", zaznam, sep="\n", end="\n\n")  # tiskne [None]
'''

item_to_add = '2021-01-01 11:10:11:1111 - BANG,\n'
print("Položka (string), kterou budu chtít vložit do seznamu 'zaznam'>", item_to_add, sep="\n", end="\n")
# zaznam_extended = zaznam.insert(0, item_to_add)
zaznam.insert(0, item_to_add)
print("(Původní) seznam 'zaznam' upravený o string 'item_to_add' na index 0>", zaznam, sep="\n")

print("\n Upravený seznam 'zaznam' vypsaný po položkách>")
for index, item in enumerate(zaznam):
    print(index, ". položka: ", item, sep="")


# 3. na poslední index přidej hodnotu:
last_item = '2021-01-01 11:14:11:1111 - BANG BANG!,\n'

# Metoda append():
# zaznam.append(last_item)
# print("Seznam 'zaznam' rozšířený o položku 'last_item'", zaznam)

# Metoda extend():
# zaznam.extend(last_item)    # ze stringu uloženého v proměnné last_item udělá nejprve seznam, jehož prvky jsou všechny znaky toho stringu.
# zaznam.extend([last_item])
# print("Seznam 'zaznam' rozšířený o položku 'last_item'", zaznam)

# Metoda insert():
zaznam.insert(len(zaznam), last_item)
print("Seznam 'zaznam' rozšířený o položku 'last_item'", zaznam)

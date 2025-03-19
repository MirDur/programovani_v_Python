'''
Rozdělení stringu
V této úloze budeš pracovat s indexy datového typu str.
Pomocí indexů a operací slicing, striding zpracuj zadané hodnoty tak, ať dostaneš:
1. Prvních 5 písmen slova 'indexování',
2. posledních 5 písmen slova 'indexování',
3. každé třetí písmeno slova 'indexování' (počínaje prvním písmenem "i"),
4. všechny výstupy zapiš přímo do funkce print,
5. výstup dále úprav podle ukázky níže.
Poznámka: Při speficikaci v hranatých závorkách použij vždy jen jedno číslo.
'''

string_to_slice = 'indexování'

# 0.
'''
print("Počet znaků ve stringu 'string_to_slice' je: ", end="")
print(len(string_to_slice))
# Procházení řetězce pomocí for smyčky. + indexování iterovaných hodnot
for index, char in enumerate(string_to_slice):
    print(f"{index}. znak: '{char}'")
print()
'''

# 1. prvních 5 písmen slova 'indexování'
print("Prvních 5 písmen:")
print(string_to_slice[:5]) # Nebo print('indexování'[0:5])

# pomocí built-in funkce slice()
'''
slice_1 = slice(5) # to samé jako slice(0, 5)
print("Vytvořený objekt 'slice_1':", slice_1)
print(string_to_slice[slice_1], end="\n\n")
'''

# 2. posledních 5 písmen slova 'indexování'
print("Posledních 5 písmen:")
print('indexování'[-5:]) # Nebo print(string_to_slice[5:])

# pomocí built-in funkce slice()
'''
# slice_2 = slice(-5, -1) # do řezu nezahrne poslední položku sekvence
slice_2 = slice(-5, None) # včetně  poslední položky sekvence
print("Vytvořený objekt 'slice_2':", slice_2)
print(string_to_slice[slice_2], end="\n\n")
'''


# 3. každé třetí písmeno slova 'indexování' (počínaje prvním písmenem "i")
print("Každé 3. písmeno (počínaje prvním) od 'i':")
print(string_to_slice[::3]) # Nebo print('indexování'[::3])

# pomocí built-in funkce slice()
'''
slice_3 = slice(None, None, 3)
print("Vytvořený objekt 'slice_3':", slice_3)
print(string_to_slice[slice_3], end="\n\n")
'''
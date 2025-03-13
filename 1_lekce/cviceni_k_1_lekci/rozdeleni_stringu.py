"""
Rozdělení stringu
V této úloze budeš pracovat s indexy datového typu str.
Pomocí indexů a operací slicing, striding zpracuj zadané hodnoty tak, ať dostaneš:
1. Prvních 5 písmen slova 'indexování',
2. posledních 5 písmen slova 'indexování',
3. každé třetí písmeno slova 'indexování' (počínaje prvním písmenem "i"),
4. všechny výstupy zapiš přímo do funkce print,
5. výstup dále úprav podle ukázky níže.
Poznámka: Při speficikaci v hranatých závorkách použij vždy jen jedno číslo.
"""

string = 'indexování'

# 0.
print("Počet znaků ve stringu <string> je: ", end="")
print(len(string))
# Procházení řetězce pomocí for smyčky
for index, char in enumerate(string):
    print(f"Index: {index}, Znak: '{char}'")
print()

# 1.
print("Prvních 5 písmen:")
print(string[0:5])
print('indexování'[:5], end="\n\n")

# 2.
print("Posledních 5 písmen:")
print(string[5:])
print('indexování'[-5:], end="\n\n")

# 3.
print("Každé 3. písmeno (počínaje prvním) od 'i':")
print(string[::3])
print('indexování'[::3], end="\n\n")
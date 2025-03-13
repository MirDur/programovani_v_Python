# V této úloze vytvoř program, který:

# 1. Vytvoř list zamestnanci, který bude obsahovat stringy 'František', 'Anna', 'Jakub', 'Klára'.
zamestnanci = ['František', 'Anna', 'Jakub', 'Klára']
print(zamestnanci)

# 2. Vypiš obsah zamestnanci za větu 'Zaměstnanci na začátku: '.
prestring_1 = 'Zaměstnanci na začátku: '
print(prestring_1, zamestnanci)

# 3. Vytvoř kopii listu zamestnanci a pojmenuj proměnnou zamestnanci_a.
zamestnanci_a = zamestnanci.copy()
# zamestnanci_a = zamestnanci[:]
# zamestnanci_a = list(zamestnanci)

# 4. Přidej do listu zamestnanci_a jména 'Bruno' a 'Anežka'.
appendage = ['Bruno', 'Anežka']
zamestnanci_a = zamestnanci_a + appendage
# zamestnanci_a.extend(['Bruno', 'Anežka'])
# zamestnanci_a += ['Bruno', 'Anežka']
# zamestnanci_a = [*zamestnanci_a, 4, 5]

# zamestnanci_a.append('Bruno')
# zamestnanci_a.append('Anežka')

# 5. vypiš obsah listu zamestnanci_a za string 'Nová jména přidána: ',
print(zamestnanci_a)
prestring_2 = 'Nová jména přidána: '
print(prestring_2, zamestnanci_a)

# 6. Vytvoř kopii listu zamestnanci a pojmenuj proměnnou zamestnanci_b.
zamestnanci_b = list(zamestnanci)
# zamestnanci_b = zamestnanci.copy()
# zamestnanci_b = zamestnanci[:]

# 7. Vlož jméno 'Bruno' na index 1.
zamestnanci_b.insert(1, 'Bruno')
print(zamestnanci_b)

# 8. Vypiš obsah proměnné zamestnanci_b za string: 'Nová jména vložena:'.
prestring_3 = 'Nová jména vložena:'
print(prestring_3, zamestnanci_b)

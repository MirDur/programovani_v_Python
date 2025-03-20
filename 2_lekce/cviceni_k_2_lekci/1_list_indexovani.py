# 0. Vytvoř list zamestnanci, který obsahuje hodnoty:
"""
    František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
"""
zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára', 'Anežka', 'Anežka', 'Anežka']


# 1. ulož poslední index ze zadaného listu zamestnanci do proměnné posledni_index

prestring_1 = "Poslední index z listu 'zamestnanci' je:"
posledni_index = (len(zamestnanci) - 1)
print(prestring_1, posledni_index)


# 2. vypiš jméno na indexu 2 za string: 'Na indexu 2 je: '
prestring_2 = 'Na indexu 2 je: '
print(prestring_2 + zamestnanci[2])
# jmeno_2 = zamestnanci[2]
# print('Na indexu 2 je: ' + jmeno_2)


# 3. vypiš jméno na posledním indexu za string: 'Na <posledni_index> indexu je:'
# prestring_3 = 'Na <posledni_index> indexu je: '
# prestring_3 = 'Na', posledni_index, 'indexu je: '
prestring_3 = 'Na ' + str(posledni_index) + ' indexu je: '
# print(prestring_3 + zamestnanci[posledni_index])
print(prestring_3 + zamestnanci[-1])


# 4. vVypiš jména od indexu 2 do 5 za string: 'V intervalu od 2 do 5 je:'
prestring_4 = 'V intervalu od 2 do 5 je:'
print(prestring_4, zamestnanci[2:6])


# 5. vypiš každý třetí prvek listu zamestnanci počínaje hodnotou 'František' za string: 'Každý třetí člen je:'
prestring_5 = 'Každý třetí člen je:'
print(prestring_5, zamestnanci[::3])

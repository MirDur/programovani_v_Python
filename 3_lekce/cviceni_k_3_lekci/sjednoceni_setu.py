'''
Sjednocení setů
cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)
'''
# 1. Zapiš všechny proměnné výše.
cisla_1 = (1, 1, 2, 3, 4)
print(type(cisla_1))
cisla_2 = (5, 6, 7, 7, 8)

# 2. Vytvoř ze zadaných proměnných sety.
set_cisel_1 = set(cisla_1)
print(type(set_cisel_1))
set_cisel_2 = set(cisla_2)

# 3. Udělá sjednocení hodnot obou nově vzniklých setů a uloží jej do proměnné sjednocene_hodnoty.
# sjednocene_hodnoty = set_cisel_1 | set_cisel_2
sjednocene_hodnoty = set_cisel_1.union(set_cisel_2)

# 4. Vypíše výsledek s ohlášením "Sjednocené hodnoty ze zadání:".
prestring = "Sjednocené hodnoty ze zadání:"
print(prestring, sjednocene_hodnoty)

'''
Řešení od Engeto>
# Vytvoř sety a udělej sjednocení jejich hodnot
# ..do proměnné "sjednocene_hodnoty"
sjednocene_hodnoty = set(cisla_1) | set(cisla_2)
'''
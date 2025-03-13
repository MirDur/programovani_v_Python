'''
Rozdíl setů
cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}
'''

# 1. Zapiš všechny proměnné výš.
cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}

# 2. Zjisti, jaké hodnoty prvního setu jsou rozdílné oproti setu druhému a uloží hodnoty do proměnné rozdil_cisel.
# rozdil_cisel = cisla_1 - cisla_2
rozdil_cisel = cisla_1.difference(cisla_2)

# 3. Vypíš výsledek s ohlášením "Rozdílné hodnoty prvního setu oproti druhému:".
prestring = "Rozdílné hodnoty prvního setu oproti druhému:"
print(prestring, rozdil_cisel)

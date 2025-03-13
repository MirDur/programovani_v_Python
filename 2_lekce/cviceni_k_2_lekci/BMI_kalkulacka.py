"""
Obecně je BMI (Body Mass Index) míra, která vyčísluje obezitu u lidí.
Rovnice výpočtu BMI: váha / výška2
Váha se udává v kilogramech a výška v metrech. Hodnoty, které z tohoto vzorečku dostaneme, škálujeme podle této tabulky:
• < 18,5	Podvýživa
• 18,5 - 25	Zdravá váha
• 25 - 30	Mírná nadváha
• 30 - 40	Obezita
• 40 <	Těžká obezita
V této úloze vytvoř program, který získá BMI uživatele Martin, který měří 200 centimerů a váží 80 kilogramů:
"""

"""
1.
Vytvoř proměnné jmeno, vaha, vyska a zadej do nich hodnoty.
"""
jmeno, vaha, vyska = "Martin", 80, 2

"""
2. 
Vytvoř proměnnou bmi a přiřaď k ní vzorec, pomocí proměnných vaha, vyska a aritmetického operátoru na druhou.
"""
# váha / výška2
bmi = vaha / vyska ** 2

"""
3. 
Vytvoř proměnnou kategorie, do které uložíš název kategorie odpovídající hodnotě BMI.
"""
kategorie = ""
# řádek výše není nutný
if bmi < 18.5:
    kategorie = "Podvýživa"
elif 18.5 < bmi < 25:
    kategorie = "Zdravá váha"
elif 25 < bmi < 30:
    kategorie = "Mírná nadváha"
elif 30 < bmi < 40:
    kategorie = "Obezita"
else:
    kategorie = "Těžká obezita"

# Alternativa>
# if bmi > 40:
#     kategorie = 'těžká obezita'
# elif bmi > 30:
#     kategorie = 'obezita'
# elif bmi > 25:
#     kategorie = 'mírná nadváha'
# elif bmi > 18.5:
#     kategorie = 'zdravá váha'
# else:
#     kategorie = 'podvýživa'
 
"""
4.
Vypiš výsledek do věty, jak je uvedeno níže.
Martin tvé BMI je 20.0, což spadá do kategorie zdravá váha.
"""
print(jmeno, "tvé BMI je", bmi, "což spadá do kategorie", kategorie)
# Hodnotu do proměnné <kategorie> bych mohl přiřazovat pomocí proměnné <bmi>.

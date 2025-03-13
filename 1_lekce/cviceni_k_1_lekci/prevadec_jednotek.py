"""
Převaděč jednotek
Cíle této úlohy bude vytvořit jednoduchý převaděč jednotek.
Převaděč bude umět následující:
1. Převod z kilogramů na libry,
2. z kilometrů na míle,
3. z litrů na galony.
Na začátek máš předepsané převodní poměry k jednotkám:
1. kg_lb = 2.20
2. km_mile = 0.62
3. l_gal = 0.26
Dále vytvoř proměnné s počtem jednotek kg_pocet , km_pocet, l_pocet:
1. kg_pocet = 80
2. km_pocet = 54
3. l_pocet = 5
Poté proměnné s výpočtem kg_vysledek, km_vysledek, l_vysledek.
Nakonec výsledky přehledně vypiš.
"""

# 1. Převod z kilogramů na libry
kg_pocet = 80
kg_lb = 2.20
kg_vysledek = kg_pocet * kg_lb
print(kg_pocet, "kg je", kg_vysledek, "lb", end="\n\n")

# 2. Převod z kilometrů na míle
km_pocet = 54
km_mile = 0.62
km_vysledek = km_pocet * km_mile
print(km_pocet, "km je", km_vysledek, "mil", end="\n\n")

# 3. Převod z litrů na galony
l_pocet = 5
l_gal = 0.26
l_vysledek = l_pocet * l_gal
print(l_pocet, "l je", l_vysledek, "gal", end="\n\n")
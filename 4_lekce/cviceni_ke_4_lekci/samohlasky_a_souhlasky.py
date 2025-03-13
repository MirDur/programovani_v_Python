'''
Samohlásky a souhlásky
V této úloze vytvoř program, který spočítá kolik samohlásek a souhlásek obsahuje zadaný string:
veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
Jednotlivé kroky, které program musí obsahovat:
'''
# 1. Vytvoř proměnnou veta, typu str, která obsahuje hodnotu: "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu".
veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
veta_bez_mezer = veta.replace(" ", "")
print("String v proměnné 'veta' obsahuje", len(veta), "znaků (včetně bílých).")
# funkce len() počítá všechny znaky v řetězci, včetně mezer (white spaces), interpunkce a speciálních znaků.
print("Bez bílých je to:", len(veta_bez_mezer))

# 2. Vytvoř proměnnou samohlasky, typu str, která obsahuje 'aeiouáéíóú'.
samohlasky = 'aeiouáéíóú'
# Chybí tam 'ě' + velký písmena jsou taky samohlásky..

# 3. Vytvoř proměnnou souhlasky, typu str, která obsahuje 'bcčdďfghjklmnňprřsštťvzžcdž'.
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
# Velký písmena jsou taky souhlásky..

# 4. Vytvoř proměnnou vysledek, typu dict, který obsahuje klíče "souhlasky" a "samohlasky". Slovník bude evidovat výskyty těchto hodnot.
vysledek = {"souhlasky" : [], "samohlasky" : []}
# print(vysledek)

# 5. Vytvoř iteraci přes všechny znaky v proměnné veta.
for _ in veta:
    pass

# 6. Pokud znak není ani samohláska, ani souhláska, tak jej přeskoč.
samohlasky_a_souhlasky = samohlasky + souhlasky
print(samohlasky_a_souhlasky)

for znak in veta:
    if znak not in samohlasky_a_souhlasky:
        continue

# 7. Pokud je znak samohláska nebo souhláska, inkrementuj ve slovníku vysledek správný klíč.
'''
for znak in veta:
    if znak in samohlasky:
        vysledek["samohlasky"].append(znak) # Přidání hodnoty do seznamu u klíče "samohlasky"
    elif znak in souhlasky:
       vysledek["souhlasky"].append(znak) # Přidání hodnoty do seznamu u klíče "souhlasky"
'''

# 8. Nakonec vypiš konečný stav podle ukázky níže.
# Počet souhlásek: 35 | Počet samohlásek: 25

for znak in veta:
    if znak not in samohlasky_a_souhlasky:
        continue
    elif znak in samohlasky:
        vysledek["samohlasky"].append(znak)
    elif znak in souhlasky:
        vysledek["souhlasky"].append(znak)

vsechny_souhlasky = vysledek["souhlasky"]
print("Všechny souhlásky zachycené ze zadaného stringu do slovníku:", vsechny_souhlasky)
pocet_souhlasek = len(vsechny_souhlasky)

vsechny_samohlasky = vysledek["samohlasky"]
print("Všechny samohlásky zachycené ze zadaného stringu do slovníku:", vsechny_samohlasky)
pocet_samohlasek = len(vsechny_samohlasky)

print("Počet souhlásek:", pocet_souhlasek, "| Počet samohlásek:", pocet_samohlasek)
print("Mezi hledanými samohláskami není/chybí znak 'ě'. \nA hledána byla pouze malá písmena.")

# Metoda isalpha() vrací True i na písmena s diakritikou.
# Engeto tu úlohu vyřešilo jinak.
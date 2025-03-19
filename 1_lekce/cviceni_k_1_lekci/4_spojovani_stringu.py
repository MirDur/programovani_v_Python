'''
Spojování stringů
V této úloze vytvoř program, který:
1. Uloží hodnotu "Lukáš", do proměnné jmeno,
2. uloží hodnotu "Dvořák", do proměnné prijmeni,
3. vytvoří proměnnou cele_jmeno, do které spojíš hodnoty v proměnných jmeno a prijmeni oddělené mezerou,
4. vytvoří proměnnou delka_jmena, která bude obsahovat délku hodnoty v proměnné cele_jmeno (započítej i přidanou mezeru),
5. vypíše hodnotu v proměnné delka_jmena (doplněnou stringem "Délka jména:"),
6. vypíše proměnnou cele_jmeno, která bude shora i zespoda ohraničená řadami rovnítek.
Poznámka. k ohraničení použij operaci opakování, znak = použij v každé řadě tolikrát, kolik znaků obsahuje string uložený v proměnné cele_jmeno
'''

# 1. ulož hodnotu "Lukáš" do proměnné jmeno
jmeno = "Lukáš"

# 2. ulož hodnotu "Dvořák" do proměnné prijmeni
prijmeni = "Dvořák"

# 3. vytvoř proměnnou cele_jmeno, do které spojíš hodnoty v proměnných jmeno a prijmeni oddělené mezerou
cele_jmeno = jmeno + " " + prijmeni
print("Celé jméno:", cele_jmeno)

# 4.
# vytvoř proměnnou delka_jmena, která bude obsahovat délku hodnoty v proměnné cele_jmeno (započítej i přidanou mezeru)
delka_jmena = len(cele_jmeno)
delka_jmena_kontrolni = len(jmeno + " " + prijmeni)

# 5. vypíš hodnotu v proměnné delka_jmena (doplněnou stringem "Délka jména:"),
print("Délka jména:", delka_jmena)
if delka_jmena == delka_jmena_kontrolni:
    pass
else:
    print("Délka jména podle kontrolního součtu je:", delka_jmena_kontrolni, ". Podle hlavního výpočtu je délka:", delka_jmena)

# 6. vypíš proměnnou cele_jmeno, která bude shora i zespoda ohraničená řadami rovnítek
# Poznámka: k ohraničení použij operaci opakování, znak = použij v každé řadě tolikrát, kolik znaků obsahuje string uložený v proměnné cele_jmeno
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * len(cele_jmeno))

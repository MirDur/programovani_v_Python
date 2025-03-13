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

# 1. 
jmeno = "Lukáš"

# 2. 
prijmeni = "Dvořák"

# 3. 
cele_jmeno = jmeno + " " + prijmeni
print("Celé jméno:", cele_jmeno)

# 4. + 5.
delka_jmena = len(cele_jmeno)
print("Délka jména:", delka_jmena)
delka_jmena_kontrolni = len(jmeno + " " + prijmeni)
print("Délka jména:", delka_jmena_kontrolni)

# 6.
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * len(cele_jmeno))

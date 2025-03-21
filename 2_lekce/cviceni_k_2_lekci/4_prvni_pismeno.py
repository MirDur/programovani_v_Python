# Tvým úkolem bude ověřit správnost prvního písmene každého dne v týdnu.
# Postup bude vypadat následovně:

# 1. Zapiš všechny proměnné o několik rádků výš (ze zadání).
vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')


# 2. Vytvoř proměnnou cislo_dne a zapiš do ní hodnotu 3.
cislo_dne = 3

# 3. Ověř, jestli hodnota v cislo_dne je v listu vstupni_cisla.
print("Je hodnota v proměnné 'cislo_dne' v seznamu 'vstupni_cisla' ? ", cislo_dne in vstupni_cisla)

# 4. + 5. Pokud není, vypiš výstup podle vzoru níže. Pokud je, vypiš zprávu "Správná vstupní hodnota!".
if cislo_dne in vstupni_cisla:
    print("Správná vstupní hodnota!")
    # ... pokud ano, hodnotu uprav a použij jako index
    # ... u 'tyden' (1 --> 'pondělí', 2 --> 'úterý', ..)
    den_tydne = tyden[cislo_dne - 1]
    if den_tydne.startswith(vstupni_pismena[cislo_dne - 1]):
        # ... pokud jsou shodné
        print("Správné písmeno")
    else:
         # ... pokud jsou různé
         print("Špatné písmeno!")   
else:
    # ... pokud ne, upozorni na chybný vstup
    print("Nesprávná hodnota v proměnnné 'cislo_dne'")    

# 6. Dále vytvoř proměnnou den_tydne a pomocí upravené hodnoty v proměnné cislo_dne, naindexuj z proměnné tyden požadovaný den (př. 1 --> "pondělí", 2 --> "úterý"),


"""
Výše je zadání, postup, řešení podle Engeto
Já si vytvořím vlastní řešení podle zadání úkolu (viz řádek 1) a pokusím se vytvořit postup řešení/zadání na základě řešení od Engeto.
"""

poradove_cislo_dne_v_tydnu = input("Zadejte prosím pořadové číslo vámi libovolně vybraného dne v týdnu (tzn. nějaké celé číslo od 1 do 7), u něhož chcete zkontrolovat první písmeno v jeho názvu: ")

if poradove_cislo_dne_v_tydnu.isdigit():
    if 0 < int(poradove_cislo_dne_v_tydnu) < 8:
            if tyden[(int(poradove_cislo_dne_v_tydnu) - 1)][0] == vstupni_pismena[(int(poradove_cislo_dne_v_tydnu) - 1)]:
                print("Vámi zvolený den v týdnu:  ", poradove_cislo_dne_v_tydnu, " - ", tyden[(int(poradove_cislo_dne_v_tydnu) - 1)], " \n \t začíná písmenem '", vstupni_pismena[(int(poradove_cislo_dne_v_tydnu) - 1)], "'.", sep="")
            else:
                print("Vámi zvolený den v týdnu:  ", poradove_cislo_dne_v_tydnu, " - ", tyden[(int(poradove_cislo_dne_v_tydnu) - 1)], " \n \t nezačíná písmenem '", vstupni_pismena[(int(poradove_cislo_dne_v_tydnu) - 1)], "'.", sep="")
    else:
        print("Vámi zvolené pořadové číslo dne v týdnu:", poradove_cislo_dne_v_tydnu, " \n \t není celé číslo z intervalu <1, 7>.")     
else:
    print("Nezadali jste celé číslo z intervalu <1, 7>.")
    
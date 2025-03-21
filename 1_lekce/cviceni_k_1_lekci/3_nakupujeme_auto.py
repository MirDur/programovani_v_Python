"""
Nakupujeme auto
Tvým úkolem bude provést různé operace s datovým typem str a int.
Úloha musí splňovat následující:
1. mercedes = 150_000
2. rolls_royce = 400_000
3. vybava = 50_000

1. Vytvoř proměnné výše,
2. Slevu do proměnné sleva_merc a její hodnotu 5000,
3. vypočítat cenu za dva Mercedesy, uložit ji do proměnné cena_2_merc,
4. vypočítat cenu za Mercedes a Rolls-Royce, uložit ji do proměnné cena_merc_a_rolls,
5. vypočítat cenu za dva Rolls-Royce s příplatkovou výbavou (každý z nich), uložit ji do proměnné cena_2_rolls_s_vybavou,
6. vypočítat cenu za Mercedes s příplatkovou výbavou, uložit ji do proměnné cena_merc_s_vybavou
7. vypočítat cenu po slevě Mercedesu a uložit ji do proměnné merc_se_slevou.
"""

# 1. vytvoř proměnné podle zadání
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

# 2. vytvoř proměnnou s názvem sleva_merc a přiřaď do ní hodnotu 5000
sleva_merc = 5000
print("Sleva na Mercedes:", sleva_merc)

# 3. vypočítat cenu za dva Mercedesy, uložit ji do proměnné cena_2_merc
cena_2_merc = mercedes * 2
print("Cena za dva Mercedesy je:", cena_2_merc)

# 4. vypočítat cenu za Mercedes a Rolls-Royce, uložit ji do proměnné cena_merc_a_rolls
cena_merc_a_rolls = mercedes + rolls_royce
print("Cena za Mercedes a Rolls-Royce:", cena_merc_a_rolls)

# 5. vypočítat cenu za dva Rolls-Royce s příplatkovou výbavou (každý z nich), uložit ji do proměnné cena_2_rolls_s_vybavou
cena_2_rolls_s_vybavou = (rolls_royce + vybava) * 2
print("Cena za dva Rolls-Royce s příplatkovou výbavou:", cena_2_rolls_s_vybavou)

# 6. vypočítat cenu za Mercedes s příplatkovou výbavou, uložit ji do proměnné cena_merc_s_vybavou
cena_merc_s_vybavou = mercedes + vybava
print("Cena za Mercedes s příplatkovou výbavou:", cena_merc_s_vybavou)

# 7. vypočítat cenu po slevě Mercedesu a uložit ji do proměnné merc_se_slevou
merc_se_slevou = mercedes - sleva_merc
print("Cena za Mercedes po slevě:", merc_se_slevou)


'''
Vytvoř takový podmínkový zápis, který bude reagovat na nesprávně zadaná hesla (viz. příklad níže):
heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
heslo_3 = "123456"      # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"
'''

heslo = input("Zadejte prosím vaše heslo: ")

# heslo_0
if len(heslo) < 1:  print("Vynechal jsi pole s heslem!")
# if not heslo: print("Vynechal jsi pole s heslem!")    

# heslo_1
elif heslo[0].isdigit():    print("Heslo nesmí začínat číselným znakem.") # číslice = číselný znak?
# metody isdecimal() a isnumeric() jsou tady taky použitelné

# heslo_2
elif heslo.isalpha(): print("Heslo musí obsahovat i číselné znaky.")
elif heslo.isnumeric(): print("Heslo musí obsahovat i písmena.")    

# elif heslo.isnumeric() or heslo.isalpha():    print("Heslo musí obsahovat jak číselné znaky, tak písmena")
# Podmínky na řádcích výše nezajistí úplně, aby v hesle byly číselné znaky i písmena zároveň.
# Obecný řešení k heslo_2 je níže>

# def obsahuje_pismena_a_cislice(text):
#     obsahuje_pismena = False
#     obsahuje_cislice = False

#     # Projdi každý znak v textu
#     for znak in text:
#         if znak.isalpha():  # Zkontroluj, zda je znak písmeno
#             obsahuje_pismena = True
#         elif znak.isdigit():  # Zkontroluj, zda je znak číslice
#             obsahuje_cislice = True

#     # Zkontroluj, zda text obsahuje i písmena, i číslice
#     return obsahuje_pismena and obsahuje_cislice


# # Testování funkce
# text = input("Zadejte řetězec: ")

# if obsahuje_pismena_a_cislice(text):
#     print("Řetězec obsahuje jak písmena, tak číslice.")
# else:
#     print("Řetězec neobsahuje jak písmena, tak číslice.")


# heslo_3
elif heslo[0].isdigit():    print("Heslo nesmí začínat číselným znakem.")
# Podmínka výše je stejná jako v případě heslo_1

# heslo_4
elif len(heslo) < 8:    print("Heslo musí obsahovat alespoň 8 znaků.")

# heslo_5
elif '@' in heslo:  print("Heslo nesmí obsahovat znak '@'.")
#elif heslo.count('@') > 0:   print("Heslo nesmí obsahovat znak '@'.")
# elif heslo.find('@') >= 0:   print("Heslo nesmí obsahovat znak '@'.")

# elif heslo.find("@") != -1:   print('Heslo nesmí obsahovat \"@\"')
# Zpětný lomítka kolem zavináče v kódu na řádku výše jsou zbytečný.

# heslo_6
else:   print("Heslo je v pořádku")

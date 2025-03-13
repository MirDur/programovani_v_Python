'''
Rozšiř slovník slovníkem
V této úloze vytvoř program, který:
'''

# 1. Vytvoří nový prázdný slovník user_1.
user_1 = {}
# user_1 = dict()

# 2. Doplní do slovníku user_1 klíč name (hodnota "Marek") a surname (hodnota "Parek").
user_1["name"] = "Marek"
user_1["surname"] = "Parek"

# A druhá možnost>
new_items = {'věk': 30, 'město': 'Praha'}
user_1.update(new_items)

# 3. Pomocí vhodné metody rozšíř stávající slovník user_1 o zadanou proměnnou user_email.
user_email = {'email':'marek.parek@gmail.com'}
user_1.update(user_email)

# 4. vypiš hodnoty nového slovníku user_1 s úvodním textem "User #01:".
prestring = "User #01:"
print(prestring, user_1)

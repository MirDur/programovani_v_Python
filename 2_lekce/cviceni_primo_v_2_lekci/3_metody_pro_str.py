# Vyzkoušej si metody pro str

# 1. Ze stringu "matous.holinka@gmail.com", získej jenom "matous.holinka".
email_adress = "matous.holinka@gmail.com"
name_and_surname = email_adress.split('@')[0]

# 2. Nahraď ve "matous.holinka" znak "." pomocí mezery " ".
name_and_surname_dotless = name_and_surname.replace(".", " ")
print(name_and_surname_dotless)

# 3. Vypiš jméno title-case, tedy "Matous Holinka".
name_and_surname_formatted = name_and_surname_dotless.title()
print(name_and_surname_formatted)

# Onliner>
print("matous.holinka@gmail.com".split("@")[0].replace(".", " ").title())
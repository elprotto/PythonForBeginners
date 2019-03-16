# Logical Operators
# or / and / not


high_income = True
good_credit = True
estrato = False

if high_income and good_credit:
    print("Los operadores son verdaderos")
else:
    print("La condicion es falsa")

if estrato and high_income and good_credit:
    print("Los operadores son verdaderos")
else:
    print("La condicion es falsa")

if estrato or high_income or good_credit:
    print("Almenos una variable es verdadera")
else:
    print("La condicion es falsa")

if not estrato:
    print("Almenos una variable es verdadera")
else:
    print("La condicion es falsa")

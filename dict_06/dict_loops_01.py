
# foreach loop

shopping_prices_dict = {'milk': 30.0, 'eggs': 120.0, 'butter': 60.0, 'bread': 10.0}

print(shopping_prices_dict)

for key, value in shopping_prices_dict.items():
    print(key, value)
    print(type(key), type(value))

    
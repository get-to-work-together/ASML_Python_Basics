pizzas = ['margarita', 'quartro stagnoini', 'vesuvius']

friend_pizzas = pizzas.copy()

pizzas.append('tonino')
friend_pizzas.append('calzone')

print('My favorite pizza\'s are:')
for pizza in pizzas:
    print(f'I like {pizza} pizza')

print('My friends favorite pizza\'s are:')
for pizza in friend_pizzas:
    print(f'I like {pizza} pizza')

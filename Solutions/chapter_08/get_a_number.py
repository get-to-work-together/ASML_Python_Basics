lowest = 1
highest = 10

while True:
    entered = input(f'Please give a number between {lowest} and {highest}: ')
    if entered.isnumeric():
        number = int(entered)
        if lowest <= number <= highest:
            break
        else:
            print(f'That number is not between {lowest} and {highest}.')
    else:
        print('That is not a number.')

print(f'{number} is a great number.')



while True:
    entered = input(f'Please give a number between {lowest} and {highest}: ')
    try:
        number = int(entered)
        if lowest <= number <= highest:
            break
        else:
            print(f'That number is not between {lowest} and {highest}.')
    except:
        print('That is not a number.')

print(f'{number} is a great number.')
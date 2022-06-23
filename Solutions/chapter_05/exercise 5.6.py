import random

age = random.randint(1,99)
print(f'Age is {age}.')

if age < 2:
    print('A baby')

elif 2 <= age < 4:
    print('A toddler')

elif 4 <= age < 13:
    print('A kid')

elif 13 <= age < 20:
    print('A teenager')

elif 20 <= age < 65:
    print('An adult')

elif age >= 65:
    print('An elder')

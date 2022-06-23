import random

alien_color = random.choice(('green', 'yellow', 'red'))

if alien_color == 'green':
    print('Yes! The color was green. You just earned 5 points')

else:
    print('The color was **NOT** green. You just earned 10 points')

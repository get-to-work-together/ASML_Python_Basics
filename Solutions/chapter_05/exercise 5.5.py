import random

alien_color = random.choice(('green', 'yellow', 'red'))

if alien_color == 'green':
    print('The color was green. You just earned 5 points')

elif alien_color == 'yellow':
    print('The color was yellow. You just earned 10 points')

elif alien_color == 'red':
    print('The color was red. You just earned 15 points')

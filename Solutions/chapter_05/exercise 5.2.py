car = 'subaru'

print('Is car == \'subaru\'? I predict True.')
print(car == 'subaru')

print('Is car != \'subaru\'? I predict False.')
print(car == 'subaru')

car = 'subaru'

print('Is car.lower() == \'subaru\'? I predict True.')
print(car.lower() == 'subaru')

number = 56

print('Is number > 10? I predict True.')
print(number > 10)
print('Is number >= 10? I predict True.')
print(number >= 10)
print('Is number < 10? I predict False.')
print(number < 10)
print('Is number <= 10? I predict False.')
print(number <= 10)
print('Is number == 10? I predict False.')
print(number == 10)
print('Is number != 10? I predict True.')
print(number != 10)

print('Is number > 10 and number < 100 ? I predict True.')
print(number > 10 and number < 100)

print('Is number < 10 or number > 100 ? I predict False.')
print(number < 10 or number > 100)

print('Is number 10,20 or 30 ? I predict False.')
print(number in (10, 20, 30))

print('Is number not 10,20 or 30 ? I predict True.')
print(number not in (10, 20, 30))

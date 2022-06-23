cubes = [x**3 for x in range(1, 11)]

print('First three numbers')
for number in cubes[:3]:
    print(number)

print('Three numbers from the middle')
for number in cubes[3:6]:
    print(number)

print('Last three numbers')
for number in cubes[-3:]:
    print(number)


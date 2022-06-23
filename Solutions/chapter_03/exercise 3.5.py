friends = ['Kim', 'Mark', 'Renske', 'Jim', 'Ragna']

print(friends)

friends.remove('Jim')
print(friends)

friends.append('Charlotte')
print(friends)

position = friends.index('Ragna')
friends[position] = 'Loes'
print(friends)

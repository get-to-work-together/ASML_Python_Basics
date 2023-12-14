

d = {'nl': '+31', 'f': '+44', 'd': '+49', 'es': '+34'}

print(d)

print(d['f'])

d['uk'] = '+40'
print(d)

d['uk'] = '+41'
print(d)


for k in sorted(d.keys()):
    print(k + ': ' + d[k])

for k, v in d.items():
    print(k + ': ' + v)


keys = ['Amsterdam','Eindhoven','Utrecht','Delft']
values = ['020','040','030','015']
d = dict(zip(keys, values))
print(d)

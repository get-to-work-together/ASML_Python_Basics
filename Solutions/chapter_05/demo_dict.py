d = dict()      # empty dict
d = {}

d = {'nl': '+31',
     'b': '+32',
     'uk': '+44'}

d['d'] = '+49'

print( list(d.keys()) )
print( list(d.values()) )
print( list(d.items()) )

for key in sorted(d.keys()):
    value = d[key]
    print(f'{key} => {value}')

for key, value in d.items():
    print(f'{key} => {value}')




def print_args(message=None, *args):
    if message:
        print(message)
    for arg in args:
        print(f'  {arg}')


def print_kwargs(message, **kwargs):
    print(message)
    print(kwargs)

print_args('My favorite colors are:', 'red', 'green', 'orange', 'blue')

print_kwargs('Printing keyword arguments', city='Eindhoven', company='ASML')

d = {'Machine ID': '67357', 'uptime': 3555, 'status':'OK'}
print_kwargs('Printing keyword arguments', **d)
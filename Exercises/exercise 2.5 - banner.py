
def banner(text):
    """Print the text as a banner"""
    n = len(text)
    print('***' + '*' * n + '***')
    print('*  ' + text    + '  *')
    print('***' + '*' * n + '***')


def create_banner(text, c = '*'):
    """A more generic function to create a banner

    arguments:
       text - the text to put in the banner
       c - the surrounding character. Defaul = '*'"""
    n = len(text)
    s  = c * (n + 6) + '\n'
    s += c + '  ' + text + '  ' + c + '\n'
    s += c * (n + 6)
    return s

def print_banner(text):
    """Print the created banner"""
    print(create_banner(text, '+'))


# ----------------------------------------------------------

if __name__ == '__main__':

    name = input('Wat is jouw naam? : ')

    banner(name)

    print_banner(name)

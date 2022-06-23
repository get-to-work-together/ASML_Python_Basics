text = input('Enter some text: ').lower()

print()
print('The complete text contains %d characters.' % len(text))
print()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

n_total = 0
for vowel in vowels:
    n = text.count(vowel)
    n_total += n

    print('Found the vowel \'%s\' %d times' % (vowel, n))

print()
print('The text contains %d vowels.' % n_total)

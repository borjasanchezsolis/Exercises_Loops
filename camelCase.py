camel = input('Write here camelCase: ')

print('snake case: ', end='')

for letter in camel:
    if letter.isupper():
        print('_' + letter.lower(), end='') 
    else:
        print(letter, end='')

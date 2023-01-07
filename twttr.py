words = input('Input: ')
print('Output: ', end='')

for letter in words:
    # excludes vowels from the word
    if not letter.lower in ['a','e','i','o','u']:
        print(letter, end='')

print()

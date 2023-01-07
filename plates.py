def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Is Valid')
    else:
        print('Invalid')


def is_valid(s):
# plate maximum of 6 characters and minimum of 2
    if len(s) < 2 and len(s)>6:
        return False
# plates must start with 2 letter
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
# numbers cannot be used in the middle of a plate, they must come at the end; 1st number cant be 0
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1
# see if the number is in the middle by checking if the number start at some point and if it doesnt end with a number then is false
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
# no periods, spaces, punctuation marks are allowed
    for character in s:
        if character in [' ', '.', '!', '?']:
            return False
# if we pass the test result True
    return True


main()
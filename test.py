integer1 = 1

try:
    integer1 = integer1 + 'Sergio'
except TypeError as error:
    print('Cannot do an addition of integer and string! Try again: ')
    print(error)

print(integer1)
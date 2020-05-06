from codecs import decode

print('Choose Wisely:')
print(
    '1. Binary to Decimal\n2. Octal to Decimal\n3. Hexadecimal to Decimal\n4. Decimal to Binary\n5. Decimal to Octal\n6. Decimal to Hexadecimal')
while True:
    choice = int(input('Enter your choice: '))
    n = input('Enter a number: ')
    if (choice == 1):
        dec = int(n, 2)
        print('Equivalent decimal number: ', dec)
    elif (choice == 2):
        dec = int(n, 8)
        print('Equivalent decimal number: ', dec)
    elif (choice == 3):
        dec = int(n, 16)
        print('Equivalent decimal number: ', dec)
    elif (choice == 4):
        binary = bin(int(n))
        print('Equivalent binary number: ', binary)
    elif (choice == 5):
        octal = oct(int(n))
        print('Equivalent binary number: ', octal)
    elif (choice == 6):
        hexa = hex(int(n))
        print('Equivalent hexadecimal number: ', hexa)
    ans = input('Do you want to continue? [Y/N]: ')

    if(ans=='Y' or ans == 'y'):
        continue
    break

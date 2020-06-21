file = open('file.txt', 'r')

while True:
    char = file.read().upper()
    if not char:
        break
    char.title()
    print(char)

file.close()

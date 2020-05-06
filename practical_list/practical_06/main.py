string = 'Python '
sub = 'Programming'

print('String: ', string)
print('Length of String: ', len(string))

print('Substring to add:', sub)

n = int(input('Enter index at which you want to insert substring: '))
string = string[:n] + sub + string[n:]
print('Modified String:', string)

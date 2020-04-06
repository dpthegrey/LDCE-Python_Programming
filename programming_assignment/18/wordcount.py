filename = "words.txt"
numLines = 0
numWords = 0
numChars = 0

# we are going to user for loop
with open(filename, 'r') as file:
    for line in file:
        # Let's create a list for words
        wordsList = line.split()
        numLines += 1
        numWords += len(wordsList)  # Just get length of wordsList list
        # getting length of line on each iteration will be our number of characters
        numChars += len(line)

# now the output
print(f"Lines: {numLines}\nWords: {numWords}\nCharacters: {numChars}")

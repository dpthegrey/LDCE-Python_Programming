
# Python program to count occurrences
# of a given character

# Method that return count of the
# given character in the string


def count(s, c):

    # Count variable
    res = 0

    for i in range(len(s)):

        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res


# string = input("Enter string:")
# ch = input("Enter character to check:")

# Driver code
string = "Can you can a can as a canner can can a can?"
ch = 'c'

print(count(string, ch))

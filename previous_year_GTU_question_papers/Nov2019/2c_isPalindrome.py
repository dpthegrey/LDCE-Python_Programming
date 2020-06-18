# A string is said to be palindrome if the reverse of the string is the same as string.
# For example, “radar” is a palindrome, but “radix” is not a palindrome.


# METHOD-1
# function which return reverse of a string
def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "radar"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

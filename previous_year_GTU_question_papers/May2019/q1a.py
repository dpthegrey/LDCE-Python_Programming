"""
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
For example factorial of 6 is 6*5*4*3*2*1 which is 720 
"""


def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n*factorial(n - 1)


num = int(input("Enter any natural number : "))

factorial = f"Factorial of {num} is {factorial(num)}"
print(factorial)

def fibonacci(n):
    a, b = 1, 1
    while a <= n:
        print(a)
        c = a + b
        a = b
        b = c

fibonacci(int(input('Enter Number:')))
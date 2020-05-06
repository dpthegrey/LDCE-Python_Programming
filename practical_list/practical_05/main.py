import numpy as np

row_first_matrix = int(input('Enter number of rows of first matrix: '))
column_first_matrix = int(input('Enter number of columns of first matrix: '))
row_second_matrix = int(input('Enter number of rows of second matrix: '))
column_second_matrix = int(input('Enter number of columns of second matrix: '))

if (column_first_matrix != row_second_matrix):
    print('Matrices cannot be multiplied.')
else:
    print('Enter elements of First matrix: ')
    a = []
    for i in range(row_first_matrix):
        x = []
        x = input().split()
        a.append(x)
    a = np.array(a, dtype=int)
    print('Enter elements of Second matrix: ')
    b = []
    for i in range(row_second_matrix):
        x = []
        x = input().split()
        b.append(x)
    b = np.array(b, dtype=int)
    c = np.dot(a, b)
    print("Dot Product is: ", c[0][0])

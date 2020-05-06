def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


g = [5, 54, 68, 56, 79, 20, 6, 8]
print(g)
sorted_list = bubbleSort(g)
print("Sorted List: ", sorted_list)

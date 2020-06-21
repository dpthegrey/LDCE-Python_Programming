# python program that sorts the list [34, 25, 81, 12, 5] using merge sort
"""
Merge Sort is a Divide and Conquer algorithm. 
It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. 
The merge() function is used for merging two halves. 
The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
"""

# Python program for implementation of MergeSort


def merge_sort(values):

    if len(values) > 1:
        m = len(values) // 2
        left = values[:m]
        right = values[m:]
        left = merge_sort(left)
        right = merge_sort(right)

        values = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                right.pop(0)
        for i in left:
            values.append(i)
        for i in right:
            values.append(i)

    return values


# Input list
a = [34, 25, 81, 12, 5]
print("Given array is")
print(*a)

a = merge_sort(a)

# Print output
print("Sorted array is : ")
print(*a)

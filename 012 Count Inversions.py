from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
"""
@author:  Infinixor 

"""
# Function to merge the two subarrays.
def merge(arr, left, mid, right):
    i = left
    j = mid
    k = 0
    invCount = 0
    temp = [0 for x in range(right - left + 1)]

    while ((i < mid) and (j <= right)):
        if (arr[i] <= arr[j]):
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            invCount += (mid - i)
            k += 1
            j += 1
    
    while (i < mid):
        temp[k] = arr[i]
        k += 1
        i += 1

    while (j <= right):
        temp[k] = arr[j]
        k += 1
        j += 1

    k = 0
    for i in range(left, right + 1):
        arr[i] = temp[k]
        k += 1

    return invCount

# Function to split two subarrays and then merge them and count inversions.
def mergeSort(arr, left, right):
    invCount = 0

    if (right > left):
        mid = (right + left) // 2

        """
            Divide the array into two parts
            total inversion count will be the
            sum of 'INVCOUNT' of left part +
            'INVCOUNT' of right part + 'INVCOUNT' of
            their combined part.
        """
        invCount = mergeSort(arr, left, mid)
        invCount += mergeSort(arr, mid + 1, right)

        # Merge both parts and count their combined inversions.
        invCount += merge(arr, left, mid + 1, right)
    
    return invCount

def getInversions(arr, n):
    return mergeSort(arr, 0, n - 1)

if __name__ == "__main__":
    # Test case 1
    arr1 = [8, 4, 2, 1]
    n1 = 4
    result1 = getInversions(arr1, n1)
    print("Test case 1:")
    print("Expected output: 6")
    print("Actual output:", result1)
    print()

    # Test case 2
    arr2 = [3, 1, 2]
    n2 = 3
    result2 = getInversions(arr2, n2)
    print("Test case 2:")
    print("Expected output: 2")
    print("Actual output:", result2)

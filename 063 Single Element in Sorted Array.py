def singleNonDuplicate(arr):
    low = 0
    n = len(arr)
    high = n - 1

    while low < high:
        mid = (low + high) // 2

        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            low = mid + 1
        else:
            high = mid

    return arr[low]


if __name__ == "__main__":
    # Test case 1
    arr1 = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    result1 = singleNonDuplicate(arr1)
    print("Test case 1:")
    print("Expected output: 2")
    print("Actual output:", result1)
    print()

    # Test case 2
    arr2 = [3, 3, 7, 7, 10, 11, 11]
    result2 = singleNonDuplicate(arr2)
    print("Test case 2:")
    print("Expected output: 10")
    print("Actual output:", result2)

def ninjaAndSortedArrays(arr1, arr2, m, n):
    i = m - 1
    j = n - 1
    lastIndex = m + n - 1
    
    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[lastIndex] = arr1[i]
            i -= 1
        else:
            arr1[lastIndex] = arr2[j]
            j -= 1
        lastIndex -= 1
    
    return arr1


if __name__ == "__main__":
    # Test case 1
    arr1_1 = [1, 3, 5, 0, 0, 0]
    arr2_1 = [2, 4, 6]
    m_1 = 3
    n_1 = 3
    result1 = ninjaAndSortedArrays(arr1_1, arr2_1, m_1, n_1)
    print("Test case 1:")
    print("Expected output: [1, 2, 3, 4, 5, 6]")
    print("Actual output:", result1)
    print()

    # Test case 2
    arr1_2 = [4, 5, 6, 0, 0, 0]
    arr2_2 = [1, 2, 3]
    m_2 = 3
    n_2 = 3
    result2 = ninjaAndSortedArrays(arr1_2, arr2_2, m_2, n_2)
    print("Test case 2:")
    print("Expected output: [1, 2, 3, 4, 5, 6]")
    print("Actual output:", result2)

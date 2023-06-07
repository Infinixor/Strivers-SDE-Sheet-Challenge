def lengthOfLongestConsecutiveSequence(arr, n):
    # To store the length of the longest consecutive sequence.
    mx = 0
    
    # To store the length of the current consecutive sequence.
    count = 0
    
    # To store all the unique elements of the array.
    sett = set(arr)
    
    for element in arr:
        if element - 1 not in sett:
            # Element is the first value of a consecutive sequence.
            j = element
            while j in sett:
                # The next consecutive element will be j + 1.
                j += 1
            # Update the maximum length of the consecutive subsequence.
            mx = max(mx, j - element)
     
    return mx


if __name__ == "__main__":
    # Test case 1
    arr1 = [100, 4, 200, 1, 3, 2]
    n1 = len(arr1)
    result1 = lengthOfLongestConsecutiveSequence(arr1, n1)
    print("Test case 1:")
    print("Expected output: 4")
    print("Actual output:", result1)
    print()

    # Test case 2
    arr2 = [0, -1, -2, 1, 2, 3]
    n2 = len(arr2)
    result2 = lengthOfLongestConsecutiveSequence(arr2, n2)
    print("Test case 2:")
    print("Expected output: 6")
    print("Actual output:", result2)

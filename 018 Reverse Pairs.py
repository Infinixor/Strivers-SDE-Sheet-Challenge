def merge(arr, start, mid, end):
    # Merging the arrays using helper arrays
    n1 = (mid - start) + 1
    n2 = end - mid
    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = arr[start + i]

    for j in range(n2):
        right[j] = arr[mid + 1 + j]

    i, j = 0, 0

    for k in range(start, end + 1):
        if j >= n2 or (i < n1 and left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2

        # Counting the pairs in the left and right subarrays.
        count = mergeSort(arr, start, mid) + mergeSort(arr, mid + 1, end)
        j = mid + 1

        for i in range(start, mid + 1):
            while j <= end and arr[i] > arr[j] * 2:
                j += 1
            count += j - (mid + 1)

        # Merging the arrays.
        merge(arr, start, mid, end)
        return count

    else:
        return 0


def reversePairs(arr, n):
    return mergeSort(arr, 0, n - 1)


if __name__ == "__main__":
    # Test case 1
    arr1 = [1, 3, 2, 3, 1]
    n1 = len(arr1)
    result1 = reversePairs(arr1, n1)
    print("Test case 1:")
    print("Expected output: 2")
    print("Actual output:", result1)
    print()

    # Test case 2
    arr2 = [2, 4, 3, 5, 1]
    n2 = len(arr2)
    result2 = reversePairs(arr2, n2)
    print("Test case 2:")
    print("Expected output: 3")
    print("Actual output:", result2)

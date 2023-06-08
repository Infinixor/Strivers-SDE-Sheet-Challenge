def commonIdx(p1, p2):
    return p1[0] == p2[0] or p1[0] == p2[1] or p1[1] == p2[0] or p1[1] == p2[1]


def fourSum(arr, target):
    n = len(arr)
    mp = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            mp[arr[i] + arr[j]] = [i, j]

    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = arr[i] + arr[j]
            if (target - sum) in mp and not commonIdx(mp[target - sum], [i, j]):
                return 'Yes'

    return 'No'


def main():
    # Test case 1
    arr1 = [1, 2, 3, 3,4, 5]
    target1 = 9
    result1 = fourSum(arr1, target1)
    print("Result for arr1 and target1:", result1)

    # Test case 2
    arr2 = [2, 4, 8, 9, 11]
    target2 = 17
    result2 = fourSum(arr2, target2)
    print("Result for arr2 and target2:", result2)


# Run the main method
if __name__ == "__main__":
    main()

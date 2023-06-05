def missingAndRepeating(arr, n):
    visited = {}
    res = []
    for i in arr:
        if i not in visited:
            visited[i] = True
        else:
            res.append(i)
    for j in range(1, len(arr) + 1):
        if j not in visited:
            res.append(j)

    return res[::-1]

def main():
    # Test case 1
    arr1 = [3, 1, 3]
    n1 = 3
    result1 = missingAndRepeating(arr1, n1)
    print("Missing and Repeating elements in arr1:", result1)

    # Test case 2
    arr2 = [4, 3, 6, 2, 1, 1]
    n2 = 6
    result2 = missingAndRepeating(arr2, n2)
    print("Missing and Repeating elements in arr2:", result2)

if __name__ == '__main__':
    main()

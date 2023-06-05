def searchMatrix(matrix, target):
    row, col = len(matrix), len(matrix[0])
    left, right = 0, row * col - 1
    while left <= right:
        mid = (left + right) // 2
        num = matrix[mid // col][mid % col]
        if num == target:
            return True
        if num > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

def main():
    # Test case 1
    matrix1 = [[1, 3, 5, 7],
               [10, 11, 16, 20],
               [23, 30, 34, 60]]
    target1 = 3
    result1 = searchMatrix(matrix1, target1)
    print("Target 3 found in matrix1:", result1)

    # Test case 2
    matrix2 = [[1, 3, 5, 7],
               [10, 11, 16, 20],
               [23, 30, 34, 60]]
    target2 = 13
    result2 = searchMatrix(matrix2, target2)
    print("Target 13 found in matrix2:", result2)

if __name__ == '__main__':
    main()

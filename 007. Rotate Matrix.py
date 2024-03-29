"""
@author:  Infinixor 

"""
def rotateMatrix(mat, n, m):
    if not len(mat):
        return

    top = 0
    bottom = len(mat) - 1

    left = 0
    right = len(mat[0]) - 1

    while left < right and top < bottom:
        prev = mat[top + 1][left]

        for i in range(left, right + 1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr

        top += 1

        for i in range(top, bottom + 1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1

        for i in range(right, left - 1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr

        bottom -= 1

        for i in range(bottom, top - 1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr

        left += 1

    return mat

def main():
    # Test case 1
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    rotated_matrix1 = rotateMatrix(matrix1, 3, 3)
    print("Rotated Matrix 1:")
    for row in rotated_matrix1:
        print(row)
    print()

    # Test case 2
    matrix2 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]]
    rotated_matrix2 = rotateMatrix(matrix2, 3, 4)
    print("Rotated Matrix 2:")
    for row in rotated_matrix2:
        print(row)
    print()

if __name__ == '__main__':
    main()

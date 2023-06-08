"""
@author: Infinixor
"""

def isValid(matrix):
    n = len(matrix)
    row = [[0 for j in range(n + 1)] for i in range(n)]
    column = [[0 for j in range(n + 1)] for i in range(n)]
    subMatrix = [[[0 for k in range(n + 1)] for j in range(3)] for i in range(3)]

    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 0:
                continue

            row[r][matrix[r][c]] += 1
            column[c][matrix[r][c]] += 1
            subMatrix[r // 3][c // 3][matrix[r][c]] += 1

            if (subMatrix[r // 3][c // 3][matrix[r][c]] > 1 or column[c][matrix[r][c]] > 1 or
                    row[r][matrix[r][c]] > 1):
                return False

    return True


def solve(matrix, i, j):
    n = len(matrix)

    if i == n - 1 and j == n:
        return True

    if j == n:
        i = i + 1
        j = 0

    if matrix[i][j] != 0:
        return solve(matrix, i, j + 1)

    for digit in range(1, n + 1):
        matrix[i][j] = digit

        if isValid(matrix):
            if solve(matrix, i, j + 1):
                return True

        matrix[i][j] = 0

    return False


def isItSudoku(matrix):
    return solve(matrix, 0, 0)


def main():
    # Example usage
    sudoku_matrix = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if isItSudoku(sudoku_matrix):
        print("The given matrix has a valid Sudoku solution.")
    else:
        print("The given matrix is not a valid Sudoku solution.")


if __name__ == "__main__":
    main()

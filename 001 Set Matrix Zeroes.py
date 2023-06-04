# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colzero = 1 #variable for keeping track of matrix[0][0] 
        cols = len(matrix[0])
        rows = len(matrix)
        for row in range(rows):
            if matrix[row][0]==0:
                    colzero=0 #if first variable of any row is zero we change colzero->0
            for col in range(1,cols):
                if matrix[row][col]==0:
                    matrix[row][0]=matrix[0][col]=0
        for row in range(rows-1,-1,-1):
            for col in range(cols-1,0,-1):
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col]=0
            if colzero==0:
                matrix[row][0]=0
matrix = [[1,1,1],[1,0,1],[1,1,1]]
ob = Solution()
print(matrix)
ob.setZeroes(matrix)
print(matrix)
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False
        return True
        
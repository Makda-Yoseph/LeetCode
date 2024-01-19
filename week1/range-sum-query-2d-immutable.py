class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,col = len(matrix),len(matrix[0])
        self.prefix = [[0]*(col+1)for r in range(row+1)]
        for r in range(len(matrix)):
            pre = 0
            for c in range(len(matrix[0])):
                pre += matrix[r][c]
                above = self.prefix[r][c+1]
                self.prefix[r+1][c+1] = pre + above
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,row2,col1,col2 = row1+1,row2+1,col1+1,col2+1
        bottomright = self.prefix[row2][col2]
        above = self.prefix[row1-1][col2]
        left =self.prefix[row2][col1-1]
        topleft = self.prefix[row1-1][col1-1]
        return bottomright - above-left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
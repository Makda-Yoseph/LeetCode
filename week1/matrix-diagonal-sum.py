class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ps, ss = 0,0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    ps += mat[i][j]
                if i+j == len(mat)-1:
                    ss += mat[i][j]
        if len(mat)%2 != 0:
            ps -= mat[len(mat)//2][len(mat)//2]
        return ps+ss
                
        
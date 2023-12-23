class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diag = defaultdict(list)
        res = []
        row = len(mat)
        col = len(mat[0])
        for r in range(row):
            for c in range(col):
                diag[r+c].append(mat[r][c])
        for k,v in diag.items():
            if k%2 == 0:
                res.extend(v[::-1])
            else:
                res.extend(v)
        return res
        

                

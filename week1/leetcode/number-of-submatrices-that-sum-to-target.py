class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        prefix = [[0]* col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                top = prefix[r-1][c] if r>0 else 0
                left = prefix[r][c-1] if c>0 else 0
                topleft = prefix[r-1][c-1] if min(r,c)>0 else 0
                prefix[r][c] = matrix[r][c]+ top +left - topleft
        print(prefix)
       
        count = 0
        for r1 in range(row):
            for r2 in range(r1,row):
                occur = defaultdict(int)
                occur[0] = 1
                for c in range(col):
                    top = prefix[r1-1][c] if r1>0 else 0
                    total = prefix[r2][c]- top
                    diff = total - target   
                    count+=occur[diff]
                    occur[total]+=1
                        
        return count

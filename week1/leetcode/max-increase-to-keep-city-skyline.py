class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        matrix = [[0]*len(grid) for n in range(len(grid))]
        maxr = []
        for i in range(len(grid)):
            maxr.append(max(grid[i]))
        maxc = []
        for i in range(len(grid)):
            mx = 0
            for j in range(len(grid)):
                mx = max(mx,grid[j][i])
            maxc.append(mx)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                matrix[i][j]= min(maxc[j],maxr[i])
                ans += matrix[i][j]-grid[i][j]
        return ans
        

        
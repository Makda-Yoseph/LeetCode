class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for l in range(len(strs[0])):
            res = []
            for c in range(len(strs)):
                res.append(strs[c][l])
            sort = sorted(res)
            if res != sort:
                count += 1
        return count
        
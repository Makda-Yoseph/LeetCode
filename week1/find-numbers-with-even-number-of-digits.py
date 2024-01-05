class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        s = list(map(str,[i for i in nums]))
        count = 0
        for i in s:
            if len(i) %2 == 0:
                count +=1
        return count
        
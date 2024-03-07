class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        ans = [-1]*(nums[-1]+1)
        for i in range(nums[-1]+1):
            val = bisect_left(nums,i)
            if val !=len(nums):
                ans[i] = abs(len(nums)-val)
        print(ans)
        for i in range(nums[-1]+1):
            if i== ans[i]:
                return i
        return -1


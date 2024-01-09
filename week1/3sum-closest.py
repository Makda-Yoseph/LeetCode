# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         l = 0
#         res = []
#         while l<len(nums):
#             x = nums[l]
#             left,right = l+1,len(nums)-1
#             while left< right:
#                 s = x+ nums[left]+ nums[right]
#                 d = abs(s-target)
#                 res.append([d,s])
#                 right -=1
#                 left +=1
#             l+=1
#         res.sort()
#         return res[0][1]
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        sa= 2**31
        res = []
        while l < len(nums):
            x = nums[l]
            left = l+1
            r = len(nums)-1
            s = 0
            while left< r:
                s =  x + nums[left] + nums[r]
                if s == target:
                    return s
                if abs(target-s) < abs(target-sa):
                    sa = s
                if s > target:
                    r -=1
                elif s< target:
                    left +=1
                else:
                    left +=1
                    r +=1
            l+=1
        return sa

        
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i=0
        ans = []
        while i < len(nums):
            num = nums[i]-1
            if num == i:
                i+=1
            else:
                if nums[num]-1 == num:
                    if nums[i] not in ans:
                        ans.append(nums[i])
                    i+=1
                else:
                
                    nums[i], nums[num]= nums[num], nums[i]
        return ans
        
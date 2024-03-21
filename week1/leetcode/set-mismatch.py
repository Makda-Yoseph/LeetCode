class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i=0
        while i < len(nums):
            num = nums[i]-1
            if num == i:
                i+=1
            else:
                if nums[num]-1 == num:
                    i+=1
                    
                else:
                
                    nums[i], nums[num]= nums[num], nums[i]
        ans = []
        for i in range(len(nums)):
            if nums[i]-1!= i:
                ans.append(nums[i])
                ans.append(i+1)
        return ans
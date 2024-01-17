class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        prefix = []
        for i in range(len(nums)):
            pre *= nums[i]
            prefix.append(pre)
        
        suff = 1
        suffix = [0]*len(nums)
        for j in range(len(nums)):
            l = len(nums)-1
            suff *= nums[l-j]
            suffix[l-j] = suff
        
        ans = []
        for k in range(len(nums)):
            if k == 0:
                ans.append(suffix[k+1])
            elif k == len(nums)-1:
                ans.append(prefix[len(nums)-2])
            else:
                ans.append((prefix[k-1]*suffix[k+1]))
        return ans

            
        
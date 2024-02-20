class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s = len(set(nums))
        count = 0
        l=r=0
        ss = defaultdict(int)
        css = 0
        while r< len(nums):
            ss[nums[r]] +=1
            if ss[nums[r]] == 1: css +=1
            while css ==s:
                count += len(nums)-r
                ss[nums[l]]-=1
                if ss[nums[l]] == 0: css -=1
                l+=1
                
            r+=1  
        return count
                    
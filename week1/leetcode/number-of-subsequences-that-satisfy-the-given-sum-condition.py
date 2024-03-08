class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)):
            c = target-nums[i]
            if c>= nums[i]:
                # l = i
                # r = len(nums)-1
                # min_val = nums[i]
                # indx = i
                # while l<=r:
                #     mid = (l+r)//2
                #     if min_val+nums[mid]<=target:
                #         if indx < mid: indx = mid
                #         l=mid +1
                #     else:
                #         r = mid -1
                indx = bisect_right(nums,c)
                
                count += 2**(indx-i-1)
        return count % (10**9 +7)
                    
        
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sumdiv(mid):
            s = 0
            for i in nums:
                s += ceil(i/mid)
            return s
        r = max(nums)
        l = 1
        ans = float('inf')
       
        while l<=r:
            mid = (r+l)//2
            m = sumdiv(mid)
            if m>threshold:
                l = mid +1

            else:
                r = mid -1
                if mid <ans:ans = mid
        return ans



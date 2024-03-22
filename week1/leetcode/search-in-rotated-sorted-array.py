class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        ans = []
        def binarysearch(l,r,nums):
            if l==r:
                if nums[l]== target:
                    ans.append(l)
                return ans
            mid = (l+r)//2
            left = binarysearch(l,mid,nums)
            right = binarysearch(mid+1,r,nums)
        binarysearch(0,len(nums)-1,nums)
        if len(ans)==0:
            return -1
        else:
            return ans[0]


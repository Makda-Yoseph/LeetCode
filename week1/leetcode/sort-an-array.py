class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half,right_half):
            l,r = 0,0
            result = []
            n = len(left_half)
            m = len(right_half)
            # print(left_half)
            while l<n and r<m:
                if left_half[l]<right_half[r]:
                    result.append(left_half[l])
                    l+=1
                else:
                    result.append(right_half[r])
                    r+=1
            result.extend(left_half[l:])
            result.extend(right_half[r:])
            return result
        def mergesort(left,right,nums):
            if left == right:
                return [nums[left]]
            mid = (left + right)//2
            left_half = mergesort(left,mid,nums)
            right_half = mergesort(mid+1,right,nums)
            return merge(left_half,right_half)
        return mergesort(0,len(nums)-1,nums)
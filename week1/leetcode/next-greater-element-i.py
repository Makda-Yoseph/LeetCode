class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = [-1]*len(nums2)
        stack = [nums2[0]]
        for i in range(1,len(nums2)):
            if nums2[i]< stack[-1]:
                stack.append(nums2[i])
            else:
               
                while stack and nums2[i]>=stack[-1]:
                    p = stack.pop()
                    out[nums2.index(p)] = nums2[i]
                    
                stack.append(nums2[i])
        ans = []
        for i in nums1:
            l = out[(nums2.index(i))]
            ans.append(l)
        return ans
        

        
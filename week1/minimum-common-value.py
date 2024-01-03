class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        u = s1.intersection(s2)
        if len(u) == 0:
            return -1
        else:
            m = list(u)
            m.sort()
            return m[0]
        
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res =[]
        dic1 = Counter(nums1)
        dic2 = Counter(nums2)
        for k ,v in dic1.items():
            if k in dic2:
                if dic1[k] < dic2[k]:
                    res.extend([k]*dic1[k])
                else:
                    res.extend([k]*dic2[k])
        return res
                

        
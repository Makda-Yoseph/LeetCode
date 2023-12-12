class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        occur = Counter(arr)
        for k,v in occur.items():
            if v > len(arr) // 4:
                return k       
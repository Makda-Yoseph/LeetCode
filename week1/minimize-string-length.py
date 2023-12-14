class Solution:
    def minimizedStringLength(self, s: str) -> int:
        occur = dict(Counter(s))
        count = 0
        for k,v in occur.items():
            count += 1
        return count
        
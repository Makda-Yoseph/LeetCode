class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        occur = {}
        mi = float('inf')
        for i in range(len(cards)):
            if cards[i] in occur:
                d = (i - occur[cards[i]]+1)
                mi = min(mi,d)
            occur[cards[i]] = i
        if mi != float('inf'):
            return mi
        else:
            return -1

        
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        r = len(cardPoints)-k
        l =0
        total = sum(cardPoints)
        window = sum(cardPoints[:r])
        res = total - window
        ma = res
        while r< len(cardPoints):
            window -= cardPoints[l]
            window +=cardPoints[r]
            res = total - window
            ma = max(ma,res)
            r += 1
            l+=1
        return ma
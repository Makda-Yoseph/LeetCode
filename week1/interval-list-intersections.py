class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l,r = 0,0
        res = []
        while l<len(firstList) and r < len(secondList):
            a,b = firstList[l]
            c,d = secondList[r]
            if b>=c and d>=a:
                res.append([max(a,c),min(b,d)])
            if b >d:
                r +=1
            else:
                l+=1
        return res
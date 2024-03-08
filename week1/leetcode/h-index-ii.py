class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            indx = bisect_left(citations,mid)
            if len(citations)-indx >= mid:
                if mid>ans:ans = mid
                print(ans)
                l= mid +1
            else:
                r= mid -1
        return ans
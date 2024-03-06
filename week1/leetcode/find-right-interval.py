class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        ans = [-1]*len(intervals)
        for i in range(len(intervals)):
            starts.append((intervals[i][0],i))
        starts.sort()
        for i in range(len(intervals)):
            l,r = 0,len(intervals)-1
            while l<=r:
                mid = (l+r)//2
                if starts[mid][0]< intervals[i][1]:
                    l=mid+1
                else:
                    r = mid-1
                    ans[i]=starts[mid][1]

        return ans
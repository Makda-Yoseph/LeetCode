class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        l,s,r =0, 0,len(tasks)-1
        ma,indx = 0,0
        while l< len(processorTime) and r >= 0:
            s = processorTime[l] + tasks[r]
            ma = max(ma,s)
            r-=1
            indx +=1
            if indx ==4:
                indx = 0
                l+=1
        return ma

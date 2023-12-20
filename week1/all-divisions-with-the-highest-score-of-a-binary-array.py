class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        occur = Counter(nums)
        count0 = 0
        count1 = occur[1]
        addn,maxim = 0,0
        maxid = {}
        result = []
        for i in range(len(nums)+1):
            if i>0 and nums[i-1] ==0:
                count0+=1
            if i>0 and nums[i-1] == 1:
                count1 -=1
            addn = count0 +count1
            if addn >= maxim:
                maxid[i] = addn
                maxim = addn
        for k,v in maxid.items():
            if v == maxim:
                result.append(k)
       
        return result

            

            

        
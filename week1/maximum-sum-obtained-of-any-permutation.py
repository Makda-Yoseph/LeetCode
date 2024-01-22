class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*len(nums)
        for r in requests:
            prefix[r[0]] += 1
            if r[1] + 1 < len(nums):
                prefix[r[1] + 1] -= 1

        pre = 0
        for i in range(len(nums)):
            pre += prefix[i]
            prefix[i] = pre
        n = sorted(nums,reverse = True)
        prefix = sorted(prefix, reverse= True)
        # print(f)
        #print(freq)
        print(n)
        print(nums)
        s = 0
        for j in range(len(nums)):
            s+=prefix[j]*n[j]
        return s % (10**9 + 7)


        
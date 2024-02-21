class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for k,v in count.items():
            if  v <=k +1:
                ans  += k+1
            else:
                ans += (ceil(v/(k+1))* (k+1))
        return ans
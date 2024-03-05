class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for s in range(len(senate)):
            if senate[s]=="R":
                r.append(s)
            else:
                d.append(s)
        n = len(senate)
        while r and d:
            rv = r.popleft()
            dv = d.popleft()
            if rv<dv:
                r.append(rv+n)
            else:
                d.append(dv+n)
        if r:
            return "Radiant"
        else:
            return "Dire"
            
            
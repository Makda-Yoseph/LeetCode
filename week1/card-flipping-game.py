class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cards = {}
        no =set()
        prob = set()
    
        for k,v in zip(fronts,backs):
            if k == v:
                if k in prob:
                    prob.remove(k)
                no.add(k) 
            if k != v:
                if k not in no:
                    prob.add(k)
                if v not in no:
                    prob.add(v)
            cards[k] = v
        print(no)
        print(prob)
          
        
        if len(prob )> 1:
            t = min(list(prob))
        elif len(prob)==1:
            t = list(prob)[0]
        else:
            t = 0
        return t
        
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        q = deque()
        
        for i in range(len(deck)):
            j = i-1
            order = []
            while j>0:
                order.append(q.popleft())
                
                j-=1
            q.appendleft(deck[i])
            for k in range(len(order)):
                q.append(order[k])
           

        return q
        
            
        
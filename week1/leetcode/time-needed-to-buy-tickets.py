class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # ans = 0
        # k = tickets[k]
        # for i in tickets:
        #     if i>=k:
        #         ans +=k
        #     else:
        #         ans += i
        # return  ans
        queue = deque()
        for i in range(len(tickets)):
            queue.append(i)
        time = 0
        while tickets[k]:
            for i in range(len(tickets)):
                d = queue.popleft()
                queue.append(d)
                if tickets[i]:
                    tickets[i]-=1
                    time +=1
                if i == k and tickets[i]==0:
                    break
        return time


        
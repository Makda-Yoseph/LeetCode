class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        a = -1
        f = False
        while t-3000  > a:
            f = True
            a = self.queue.popleft()
        if f:
            self.queue.appendleft(a)
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
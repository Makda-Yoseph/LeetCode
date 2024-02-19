class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        node = ListNode(homepage)
        self.head = node
        self.curr = node
    def visit(self, url: str) -> None:
        node = ListNode(url)
        # if self.curr.next.prev:
        #     self.curr.next.prev = None
        # self.curr.next = None
        self.curr.next = node
        node.prev= self.curr
        self.curr = node
    def back(self, steps: int) -> str:
        temp = self.curr
        while temp.prev and steps:
            temp = temp.prev
            steps -=1
        self.curr = temp
        return temp.val

    def forward(self, steps: int) -> str:
        temp = self.curr
        while temp.next and steps:
            temp = temp.next
            steps -=1
        self.curr = temp
        return temp.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return None
        f = 0 
        fast= slow = head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                f = 1
                break
        if f == 1:
            fast = head
            while fast:
                if fast == slow:
                    return slow
                fast = fast.next
                slow = slow.next
        return None
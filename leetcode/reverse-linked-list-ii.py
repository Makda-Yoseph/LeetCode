# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        prev = None
        curr = head
        ct = 1
        while ct < left:
            prev = curr
            curr = curr.next
            ct += 1
        start = prev
        end = curr
        while ct <= right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            ct += 1
        if start:
            start.next = prev
        else:
            head = prev
        end.next = curr
        
        return head

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            size +=1
            temp = temp.next
        temp = head
        for i in range(size):
            curr = head
            for j in range(i):
                if curr.val > temp.val:
                    s = temp.val
                    temp.val = curr.val
                    curr.val = s
                curr = curr.next
            temp = temp.next
        return head
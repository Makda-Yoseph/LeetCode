# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr,size = head,0
        while curr:
            curr = curr.next
            size +=1
        extend, part = size%k, size//k
        output = []
        curr = head
        for i in range(k):
            output.append(curr)
            for j in range(part -1 + (1 if extend else 0)):
                if not curr: break
                else:
                    curr = curr.next
            extend -=(1 if extend else 0)
            if curr:
                curr.next,curr = None, curr.next
        return output
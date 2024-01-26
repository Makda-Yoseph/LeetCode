# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        li1,li2,prev= list1,list2,None
        if not li1 and not li2:
            return li1
        elif not li1:
            return li2
        elif not li2:
            return li1
            
        if  li1 and li2 :
            if li1.val<= li2.val:
                prev = li1
                li1= li1.next

            else:
                prev = li2
                li2= li2.next
        head = prev
        print(prev)
        while li1 and li2:
            if li1.val<=li2.val:
                prev.next = li1
                prev =li1
                li1 = li1.next
                
            else:
                prev.next = li2
                prev = li2
                li2 = li2.next
        print(prev)
        if li1!= None:
            prev.next = li1
        elif li2!= None:
            prev.next = li2
        return head
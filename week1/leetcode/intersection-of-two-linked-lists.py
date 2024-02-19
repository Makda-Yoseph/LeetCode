# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1,temp2 = headA,headB
        l1,l2 = 0,0
        while temp1:
            l1 +=1
            temp1= temp1.next
        while temp2:
            l2 +=1
            temp2 = temp2.next
        diff = abs(l2-l1)
        if l2>l1:
            temp1,temp2 = headA,headB
            while diff:
                temp2 = temp2.next
                diff -=1
        elif l1>l2:
            temp1,temp2 = headA,headB
            while diff:
                temp1 = temp1.next
                diff -=1
        else:
            temp1,temp2 = headA,headB
       
        while temp2 :
            if  temp2 == temp1:
                return temp1
            temp2 = temp2.next
            temp1 = temp1.next
            
        return None
                
    
        
        
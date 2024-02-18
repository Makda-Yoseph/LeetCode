class ListNode:
    def __init__(self, value=0, next_node=None):
        self.val = value
        self.next = next_node

class MyLinkedList:
    def __init__(self):
        # A dummy node is used to simplify edge cases by providing a non-null next node.
        self.dummy = ListNode()
        # Counter for the number of elements in the linked list.
        self.size = 0

    def get(self, index: int) -> int:
        # If index is out of bounds, return -1.
        if index < 0 or index >= self.size:
            return -1
      
        # Traverse the linked list to the given index.
        current = self.dummy.next
        for _ in range(index):
            current = current.next
        # Return the value at the given index.
        return current.val

    def addAtHead(self, val: int) -> None:
        # Delegate to addAtIndex to add an element at the head (index 0).
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        # Delegate to addAtIndex to add an element at the tail (end of the list).
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # If index is greater than the size, don't perform the add.
        if index > self.size:
            return
      
        # Find the predecessor node (pre) for the index where new node will be added.
        predecessor = self.dummy
        for _ in range(index):
            predecessor = predecessor.next
      
        # Insert new node with value `val` after predecessor node.
        new_node = ListNode(val, predecessor.next)
        predecessor.next = new_node
        # Increment size after addition.
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # If index is out of range, do nothing.
        if index < 0 or index >= self.size:
            return
      
        # Find the predecessor node of the node to be deleted.
        predecessor = self.dummy
        for _ in range(index):
            predecessor = predecessor.next
      
        # Skip over the node at the index to delete it.
        to_delete = predecessor.next
        predecessor.next = to_delete.next
        # Optional: clear the next reference of the deleted node.
        to_delete.next = None
        # Decrement size after deletion.
        self.size -= 1
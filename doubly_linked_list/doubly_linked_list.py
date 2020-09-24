"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node  = ListNode(value, None, self.head)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        elif self.head is self.tail:
            removed = self.head
            self.head = None
            self.tail = None
            self.length -= 1 
            return removed.value
        else:
            removed = self.head
            self.head = removed.next
            self.head.prev = None
            self.length -= 1 
            return removed.value
        
    

        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail, None)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
        if self.head is self.tail:
            removed = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1 
            return removed
        else:
            removed = self.tail
            self.tail = removed.prev
            self.tail.next = None
            self.length -= 1 
            return removed.value


            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.tail is node:
            node.prev.next = None
        else: 
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if not self.head:
            return None
        if self.head is self.tail:
            return None
        elif self.tail is node:
            return None
        elif self.head is node:
            self.head = node.next
            self.head.prev = None
            if self.head is self.tail:
                self.head.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail = node



    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return None
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            self.head.prev = None
        elif self.tail is node:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        maxV = self.head.value
        currentNode = self.head
        while currentNode.next:
            if maxV < currentNode.next.value:
                maxV = currentNode.next.value
            currentNode = currentNode.next
        return maxV

num1 = ListNode(1)
list1 = DoublyLinkedList(num1)
     
list1.add_to_head(40)
list1.move_to_end(list1.head)
list1.add_to_tail(4)
list1.move_to_end(list1.head.next)
print("head", list1.head.value)
print("tail", list1.tail.value)
print("heads next", list1.head.next.value)

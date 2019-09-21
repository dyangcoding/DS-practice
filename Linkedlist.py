class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # insert given node at the front of the linked list
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node 
    
    # insert node after a given node
    def insertAfter(self, node, val):
        if (node is None):
            print('the given node is none, break')
            return
        new_node = Node(val)
        new_node.next = node.next
        node.next = new_node
    
    # insert node at the end of the linked list
    def append(self, val):
        node = Node(val)
        if (self.head is None):
            self.head = node
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = node
    
    def printList(self):
        temp = self.head  
        while (temp is not None):
            print(str(temp.val) + ' -> ', end='')
            temp = temp.next
        print('None')

if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    # Insert 6.  So linked list becomes 6->None 
    llist.append(6) 
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
    llist.push(7); 
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
    llist.push(1); 
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
    llist.append(4) 
  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
    llist.insertAfter(llist.head.next, 8) 
  
    print('Created linked list is:') 
    llist.printList() 
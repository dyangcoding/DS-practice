from Linkedlist import LinkedList
from Linkedlist import Node

# Write a function that moves the last element to the front 
# in a given Singly Linked List.

# appoach 
# find the second last node and set the next ref to none

def moveLast(list: LinkedList) -> LinkedList:
    if (not list or not list.head):
        return None
    temp = list.head
    while (temp.next):
        if (not temp.next.next):
            last = temp.next
            last.next = list.head
            temp.next = None
            list.head = last
            break
        temp = temp.next
    return list

if __name__=='__main__':
    llist = LinkedList()  
  
    # test remove duplicates in a sorted list

    llist.push(20)  
    llist.push(13)  
    llist.push(13) 
    llist.push(11) 
    llist.push(11) 
    llist.push(11) 
    print ("Created Linked List: ") 
    llist.printList()  
    print() 
    print("Linked List after moving",  
                "last element to front:") 
    llist = moveLast(llist)
    llist.printList() 
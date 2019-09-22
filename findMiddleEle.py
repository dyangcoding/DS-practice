from Linkedlist import LinkedList
from Linkedlist import Node


# find middle element of a linked list
# if list contains even elements, return the second middle element


# approach 1 
# traverse the given list and calculate the length of the list
# then traverse the list again and get the middle elememt 

def findMidEle_1(list: LinkedList) -> int:
    length = list.length()
    mid_idx = length // 2
    temp = list.head
    idx = -1
    while (temp):
        idx = idx + 1
        if (idx == mid_idx):
            return temp.val
        temp = temp.next

# approach 2
# using doule pointer
# both start by the header, the slow one increment by one element
# and the faster pointer by two 
# wenn the faster pointer arrives the last element, then the slow
# one finds the middle element

def findMidEle_2(list: LinkedList) -> int:
    if (list.head is None):
        return
    temp = list.head
    slow, fast = temp, temp
    while (slow and fast and fast.next):
        fast_next = fast.next
        fast = fast_next.next
        slow = slow.next

    return slow.val
    
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
  
    # Insert 10 at the end. So linked list becomes 1->7->6->4->10->None
    llist.append(10)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> 10 ->None 
    llist.insertAfter(llist.head.next, 8) 

    # print list
    llist.printList()

    # find middle element 
    print(findMidEle_1(llist))
    print('-------------')
    print(findMidEle_2(llist))
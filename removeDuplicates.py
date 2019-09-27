from Linkedlist import LinkedList
from Linkedlist import Node

# Write a function which takes a list sorted in 
# non-decreasing order and deletes any duplicate nodes from the list.

# approach 
# compare current data of node with next one by each iteration  
# if duplicate found, reset next ref 

def removeDup(list: LinkedList) -> LinkedList:
    if (not list or not list.head):
        return None
    temp = list.head
    while (temp.next):
        if (temp.val == temp.next.val):
            new = temp.next.next
            temp.next = new
        else:
            temp = temp.next
    return list

# Write a removeDuplicates() function which takes a list 
# and deletes any duplicate nodes from the list. The list is not sorted. 

# approach 1 
# first sort the list and use the method above

# approach 2
# use a hash map to check duplicate data

def removeDuplicates(list: LinkedList) -> LinkedList:
    if (not list or not list.head):
        return None
    temp = list.head
    vals = set()
    vals.add(temp.val)
    while (temp.next):
        if (temp.next.val in vals):
            new = temp.next.next
            temp.next = new
        else:
            vals.add(temp.next.val)
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
    print("Linked List after removing",  
                "duplicate elements:") 
    llist = removeDup(llist)
    llist.printList()  

    # test remove duplicates in an unsorted list
    list = LinkedList()
    list.append(10)
    list.append(12)
    list.append(11)
    list.append(11)
    list.append(12)
    list.append(11)
    list.append(10)
    print ("Created Linked List: ") 
    list.printList()
    print("Linked List after removing",  
                "duplicate elements:") 
    list = removeDuplicates(list)
    list.printList()
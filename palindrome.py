from Linkedlist import LinkedList
from Linkedlist import Node

# check if a linked list is a palindrome

# approach 1
# stack
# traverse list and store element in a stack
# traverse list again and pop element from stack by each interation
# if all nodes matched, then return true, otherwise false

def checkPalindro(list: LinkedList) -> bool:
    if (not list):
        return False
    if (list.length() <= 1):
        return True
    temp = list.head
    stack = []
    while (temp):
        stack.append(temp.val)
        temp = temp.next
    temp = list.head
    while (temp):
        ele = stack.pop()
        if (temp.val != ele):
            return False
        temp = temp.next
    return True

# approach 2
# string reverse
# traverse list and store data as a string
# reverse string and compare both
# if matched, return true, otherwise false

def checkPalindro_2(list: LinkedList):
    if (not list):
        return False
    if (list.length() <= 1):
        return True
    temp = list.head
    re = ''
    while (temp):
        re = re + temp.val
        temp = temp.next
    return re == re[::-1]

if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    # Insert a.  So linked list becomes 6->None 
    llist.append('a') 
  
    # Insert b at the beginning. So linked list becomes b->a->None 
    llist.push('b'); 
  
    # Insert b at the beginning. So linked list becomes b->a->b->None 
    llist.append('b'); 

    # print list
    llist.printList()

    print(checkPalindro(llist))
    print('-------------')
    print(checkPalindro_2(llist))
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    slow=head
    fast=head
    flag=0
    while (fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
        
        if slow ==fast:
            flag=1
            break
    return flag
    

''' using list
def has_cycle(head):
    visted=[]
    curr=head
    flag=0
    while curr:
        if curr.data in visted: 
            flag=1
            break
        else:
            visted.append(curr.data)
            curr=curr.next
    return flag
'''

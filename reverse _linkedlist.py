"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""


def ReversePrint(head):
    prev=None
    curr=head
    while(curr):
        next2=curr.next
        curr.next=prev
        prev=curr        
        curr=next2
    
    while (prev):
        print prev.data
        prev= prev.next



''' Recursive approach 
def ReversePrint(head):

    if head is None:
        return
    if head.next is not None:
        ReversePrint(head.next)
    print head.data
    
''''

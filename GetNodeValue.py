'''
You’re given the pointer to the head node of a linked list and a specific position. Counting backwards from the tail node of the linked list, get the value of the node at the given position. A position of 0 corresponds to the tail, 1 corresponds to the node before the tail and so on.

Input Format 
You have to complete the int GetNode(Node* head, int positionFromTail) method which takes two arguments - the head of the linked list and the position of the node from the tail. positionFromTail will be at least 0 and less than the number of nodes in the list. You should NOT read any input from stdin/console.

Constraints 
Position will be a valid element in linked list.

Output Format 
Find the node at the given position counting backwards from the tail. Then return the data contained in this node. Do NOT print anything to stdout/console.

Sample Input

1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 0
1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 2
Sample Output

6
3


'''

#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    curr=head
    len1=-1
    prev=Node()
    
    while(curr):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
        
    counter=0
    flag=None
    #prev=head1.next
    
    while(prev):
        if counter==position:
                flag=prev.data
                break
        else:
            prev=prev.next
            counter=counter+1
    return flag




''' 
#better 
def GetNode(head, position):
    vals = []
    while head != None:
        vals.append(head.data)
        head = head.next
    return vals[len(vals)-position-1]
'''

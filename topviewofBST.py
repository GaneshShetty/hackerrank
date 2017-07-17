'''


You are given a pointer to the root of a binary tree. Print the top view of the binary tree. 
Top view means when you look the tree from the top the nodes you will see will be called the top view of the tree. See the example below. 
You only have to complete the function. 
For example :

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Top View : 1 -> 2 -> 5 -> 6

'''



def topview(root,order=0):
  if root is None:
    return
  else:
      if order<0:
          topview(root.left,-1)
      #display current data
      print root.data
      if order>=0:
        topview(root.right,+1)

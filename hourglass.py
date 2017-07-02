'''
Context 
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

Task 
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Input Format

There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

 contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4
Submissions: 88418
Max Score: 15
Difficulty: Easy
Rate This Challenge:
    
More
Current Buffer (saved locally, editable)     
'''





import sys

arr =[]
for arr_i in xrange(6):
    arr_tmp=map(int,raw_input().strip().split(' '))
    #print arr_tmp
    arr.append(arr_tmp)
    
'''
for i in range(len(arr[0])):
    print i
    print arr[i]
    print "--------------------------"

print "####################################"

print len(arr)
'''

#Here loop runs (R-2)*(C-2) times considering
# different top left cells of hour glasses.
    
maxsum=0
for i in range(len(arr)-2):
    for j in range(len(arr[0])-2):
        sum1= (arr[i][j]+arr[i][j+1]+arr[i][j+2]
               +arr[i+1][j+1]+
               arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
        print sum1
        print "-------------------------------"
        if sum1 > maxsum:
               maxsum=sum1

print "sum is "+ str(maxsum)



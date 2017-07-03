'''

There is a collection of  strings ( There can be multiple occurences of a particular string ). Each string's length is no more than  characters. There are also  queries. For each query, you are given a string, and you need to find out how many times this string occurs in the given collection of  strings.

Input Format

The first line contains , the number of strings.
The next  lines each contain a string.
The nd line contains , the number of queries.
The following  lines each contain a query string.

Constraints

 
 
    

Sample Input

4
aba
baba
aba
xzxb
3
aba
xzxb
ab
Sample Output

2
1
0
Explanation

Here, "aba" occurs twice, in the first and third string. The string "xzxb" occurs once in the fourth string, and "ab" does not occur at all.

a=['xc','xc','b','b','b','c']
d={}
for item in a:
    d[item]=d.get(item,0)+1

b=['xc','c','e']

for i in b:
    if i in d.keys():
        print str(i) +" : "+ str(d.get(i))
    else:
        print str(i) + " : "+ str(0)
        
print "#############33"
for k in b:
    print a.count(k)

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())

list1=[]
list2=[]
for _ in range(N):
    list1.append(raw_input())

Q=int(raw_input())
for _ in range(Q):
    list2.append(raw_input())


for i in list2:
    print list1.count(i)

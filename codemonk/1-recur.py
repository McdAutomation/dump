#https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/awesome-sequence-3/

K = int(input())
arr = list(map(int,input().split()))
Q = int(input())
'''def findSeq(s):
    L = len(s)
    s.extend(s)
    R = len(s)
    for i in range(L,R):
        s[i] += arr[(i%K)]
'''
'''def findSeq(s):
    L = len(s)
    R = 2*L
    for i in range(L,R):
        s.append(s[i-L]+arr[(i%K)])
'''
'''
for i in range(Q):
    numOfTimes = int(input())
    while len(s) <= numOfTimes:
        findSeq(s)
    print(s[numOfTimes]%(10**9+7))
'''


def findSeq(numOfTimes):
     #+ arr[(numOfTimes%K)]
    if numOfTimes == 0:
     return 1
    size = 1
    while numOfTimes>size:
        size*=2
    #print("size->",size,"numOfTimes->",numOfTimes,"added->",arr[(numOfTimes%K)])
    #print("this->",(numOfTimes%K))
    return findSeq((size//2) - (size%numOfTimes)) + \
                    (arr[(numOfTimes%K)])


for i in range(Q):
    numOfTimes = int(input())
    x = findSeq(numOfTimes)
    print(x%(10**9+7))

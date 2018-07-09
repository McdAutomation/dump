# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/battlefield-13/
from sys import stdin, stdout
T = int(stdin.readline())
for t in range(T):
    N = int(stdin.readline())
    arr=[]
    arr.extend(stdin.readline())
    num_char = {'D':0,'K':0}
    check = False
    for i in range(N):
        num_char[arr[i]] += 1
    nd = 0
    nk = 0
    nd_max = 0
    nk_max = 0
    for i in range(num_char['D']):
        nd += (1 if arr[i] == 'D' else 0 )
    for i in range(num_char['K']):
        nk += (1 if arr[i] == 'K' else 0 )

    j = 0
    nd_max = nd
    for i in range(num_char['D'],N):
        nd += (1 if arr[i] == 'D' else 0)
        nd -= (1 if arr[j] == 'D' else 0)
        if nd > nd_max:
            nd_max = nd
        j += 1
    j = 0
    nk_max = nk
    for i in range(num_char['K'],N):
        nk += (1 if arr[i] == 'K' else 0)
        nk -= (1 if arr[j] == 'K' else 0)
        if nk > nk_max:
            nk_max = nk
        j += 1
    max_ = 0
    if (num_char['K'] - nk_max)<(num_char['D'] - nd_max):
        max_ = (num_char['K'] - nk_max)
    else:
        max_ = num_char['D'] - nd_max
    print(max_)

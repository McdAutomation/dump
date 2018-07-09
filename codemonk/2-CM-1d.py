#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/golf/distinct-count-2/
from collections import Counter
N = int(input())
arr = list(map(int,input().split()))

ctr = Counter(arr)
max = -1
k = 0
for key in ctr:
    if ctr[key] > max:
        max = ctr[key]
        k = key
    elif ctr[key] == max:
        if key < k:
            k = key
            max = ctr[key]
        else:
            pass
print(k)

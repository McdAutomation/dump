# not solved
# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/segment-tree-baby/
from sys import stdin, stdout, maxsize
N, T = tuple(map(int,stdin.readline().split()))
arr = [0]*(N+1)
ls = []
print(N,T)
for t in range(T):
    a, b, sum_ = tuple(map(int,stdin.readline().split()))
    print(a,b,sum_)
    arr[a-1] += sum_
    arr[b] -= sum_
    ls.append( [a,b,sum_] )

max_indi = 0
min_indi = sys.maxsize
for i in range(1,N):
    arr[i] += arr[i-1]
    if arr[i] > max_indi:
        max_indi = arr[i]


new_arr = []

for t in range(T):
    ll = ls[t][0]-1
    lr = ls[t][1]
    num_to_sub = ls[t][2]
    for i in range(ll, lr):
        if (arr[i]) == max_indi:
            if (arr[i] - num_to_sub)
            new_arr.append((arr[i]-ls[t][2]))

print((new_arr))

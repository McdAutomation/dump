# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/professor-and-his-operations/
from sys import stdin, stdout
N = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
track = [0]*(N+1)
T = int(input())
for t in range(T):
    a, b = tuple(map(int,stdin.readline().split()))
    track[a-1] += 1
    track[b] -= 1

for i in range(1,N):
    track[i] += track[i-1]

for i in range(0,N):
    if track[i]%2 == 1:
        arr[i], arr[N-i-1] = arr[N-i-1], arr[i]


stdout.write(" ".join([str(s) for s in arr]))

from heapq import *

inputs = list(map(int,input().split(" ")))
Q = inputs[0]
K = inputs[1]

hp = []

for i in range(K):
    x = list(map(int,input().split(" ")))
    heappush(hp,-(x[1]**2 + x[2]**2))

Q = Q - K

for i in range(Q):
    x = list(map(int,input().split()))
    if x[0] == 2:
        print(-hp[0])
    elif x[0] == 1:
        var = x[1]**2 + x[2]**2
        if var < -hp[0]:
            heappop(hp)
            heappush(hp,-var)

from heapq import *
import sys
Q = int(input())
arr = []
deleted = []
hp_min = []
hp_max = []
for i in range(Q):

    s = input()
    if s[0] == '1':
        temp = list(map(int,s.split(" ")))
        heappush(hp_min,temp[1])
        heappush(hp_max,-temp[1])
    elif s[0] == '2':
        temp = list(map(int,s.split(" ")))
        if (temp[1] not in hp_min) or (-temp[1] not in hp_max):
            print(-1)
        elif hp_min[0] == temp[1]:
            heappop(hp_min)
        elif -hp_max[0] == temp[1]:
            heappop(hp_max)
        else:
            deleted.append(temp)
    elif s[0] == '3':
        if -hp_max[0] in deleted:
            while(-hp_max[0] in deleted):
                heappop(hp_max)
        print(-hp_max[0])
    elif s[0] == '4':
        while True:
            if hp_min[0] in deleted:
                heappop(hp_min)
            else:
                 break
        print(hp_min[0])

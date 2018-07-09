#https://www.hackerearth.com/problem/algorithm/sherif-and-the-bombs-7/
import math
T = int(input())
arr = [[] for i in range(T)]
for t in range(T):
    arr[t].append(list(map(int,input().split())))
count = 0
for t in range(T):
    x1 = arr[t][0]+arr[t][2]
    y1 = arr[t][1]+arr[t][2]
    x = arr[t][0]
    y = arr[t][1]
    for i in range(x,x1):
        for j in range(y,y1):
            if math.sqrt( (x1-x)**2 + (y1-y)**2 ) < r:
                count += 1

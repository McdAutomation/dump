# https://www.hackerearth.com/zh/practice/data-structures/arrays/1-d/practice-problems/algorithm/can-you-solve-it/

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    max=0
    for i in range(N):
        for j in range(i,N):
            temp = abs(arr[i]-arr[j])+abs(i-j)
            if temp > max:
                max = temp

    print(max)

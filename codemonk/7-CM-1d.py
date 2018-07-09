#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/i-demand-trial-by-combat-13/
import sys
import numpy as np

T = int(input())
for t in range(T):
        N, round = tuple(map(int,input().split()))
        arr = list(map(int,sys.stdin.readline().strip().split()))
        temp = -1
        for j in range(round):
            count = 0
            temp = -1
            for i in range(N):
                if i==0 and arr[i+1]==1:
                    temp = arr[i]
                    arr[i]=1
                elif temp==1 and i==N-1:
                    arr[N-1]=1

                elif temp == 1 and arr[i+1] == 1:
                    temp = arr[i]
                    arr[i] = 1

                else:
                    temp = arr[i]
                    arr[i] = 0
                if arr[i] == 0:
                    count += 1
            if count == N:
                break
        for k in range(N):
            print(arr[k],end=" ")
        print()

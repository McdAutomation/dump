#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/
import numpy as np
N = int(input())
ctr = np.zeros(shape=(N))
arr = list(map(int,input().split()))
max = -1
for i in range(N-1,-1,-1):
        if arr[i] > max:
            max = arr[i]
            ctr[i] = 1
for i in range(N):
    if ctr[i] == 1:
        print(arr[i],end=" ")

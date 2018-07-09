#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/play-with-numbers-2/
N,T = tuple(map(int,input().split()))
arr = list(map(int,input().split()))
import numpy as np
x = np.zeros(shape=(N))
x[0] = arr[0]

for i in range(1,N):
    x[i] = arr[i] + x[i-1]

for i in range(T):
    a, b = tuple(map(int,input().split()))
    if a!=1:
        print(int((x[b-1]-x[a-2])//(b-a+1)))
    elif a==1:
        print(int((x[b-1])//(b)))

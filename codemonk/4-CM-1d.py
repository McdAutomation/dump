#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/x-4/
import numpy as np
T = int(input())
for t in range(T):
    N = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    c_1 = np.zeros(shape=101)
    c_2 = np.zeros(shape=101)
    for i in range(N):
        c_1[arr1[i]] += 1
        c_2[arr2[i]] += 1
    max1=-1
    max2=-1

    '''for i in range(N):
        if c_1[arr1[i]] > maxvalue1:
            maxvalue1 = c_1[arr1[i]]
            max1 = arr1[i]
        if c_2[arr2[i]] > maxvalue2:
            maxvalue2 = c_2[arr2[i]]
            max2 = arr2[i]
'''
    for i in range(101):
        if c_1[i] >= max1:
            max1 = c_1[i]
            maxvalue1=i
        if c_2[i] >= max2:
            max2 = c_2[i]
            maxvalue2=i
    if maxvalue1 > maxvalue2:
        print("Rupam")
    elif maxvalue2 > maxvalue1:
        print("Ankit")
    else:
        print("Tie")
    #print("Rupam") if max1 > max2 else print("Ankit") if max2>max1 else print("Tie")

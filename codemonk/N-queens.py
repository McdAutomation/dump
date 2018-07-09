#N-Queens
#https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/


size = int(input())
import numpy as np
arr = np.zeros(shape=(size,size))

def isAttacked(arr,a,b):
    for i in range(size):
        if arr[i][b] == 1:
            return True
        for j in range(size):
            if ((i + j)==(a+b)) and (arr[i][j]==1):
                return True
            elif ((i - j)==(a-b)) and (arr[i][j]==1):
                return True

    for j in range(size):
        if arr[a][j] == 1:
            return True
'''

#codemonk
import numpy as np
N = int(input())
arr = np.zeros(shape=(N,N))
Q = N- 1
def isAttacked(a,b):
    for i in range(N):
        for j in range(N):
            if (i-j) == (a-b):
                if arr[i][j] == 1:
                    return True
            if (i+j) == (a+b):
                if arr[i][j] == 1:
                    return True
    for i in range(N):
        if arr[i][b] == 1:
            return True
        if arr[a][i] == 1:
            return True

####
"""
    for i in range(N):
        for j in range(N):
            if ((i==r) | (j==c)) \
                | ((i+j)==(r+c)) | ((i-j) == (r-c)):
                if(arr[i][j]==1):
                    return True
    return False
"""
#####
def N_Queens(Q):
    if Q==-1:
        return True

    for j in range(N):
        if isAttacked(j,Q) :
            continue
        arr[j][Q]=1
        #print(arr)
        if N_Queens(Q-1):
            return True
        arr[j][Q] = 0
    return False
if N_Queens(Q):
    for i in range(N):
        for j in range(N):
            print(int(arr[i][j]),end=" ")
        print("")
else:
    print("Not possible")

'''

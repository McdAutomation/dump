# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/nice-arches-1/
T = int(input())


def rec_func(arr,N,num,i,j):
    if (i<-1 or i > N-1):
        if num == N:
            return 1
        else:
            return 0
    if arr[i] == arr[i+1]:
        num = 2 + rec_func(arr,N,num,i-1,i+2)
    elif arr[i] == arr[i-1]:
        num = 2 + rec_func(arr,N,num,i+1,i-2)


for t in range(T):
    arr = []
    arr.extend(input())
    count = 0
    count += rec_func(arr,len(arr),0,0)
    print(rec_func())

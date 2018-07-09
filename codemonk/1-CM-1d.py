import sys
T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    max = 0
    subset = -sys.maxsize
    for i in range(N):
        print((i+1)*(arr[i]+max) )
        if ((i+1)*(arr[i]+max) > subset):
            max = (arr[i]+max)
            subset = (i+1)*max
        else:
            break
    print(subset)

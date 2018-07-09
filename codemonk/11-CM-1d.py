# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/unique-subarrays/

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    j = 0
    unique = {}
    count = 0
    for i in range(0,N):
        while j<N and unique.get(arr[j],0) == 0:
            unique[arr[j]] = 1
            j += 1
        count += (j-i)*(j-i+1)//2
        unique.pop(arr[i])
    print(count)

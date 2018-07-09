#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/maximize-the-earning-137963bc-323025a6/

T = int(input())
for t in range(T):
    N, price = tuple(map(int,input().split()))
    arr = list(map(int,input().split()))
    max = -1
    num_of_buildings = 0
    for i in range(N):
        if arr[i] > max:
            max = arr[i]
            num_of_buildings += 1
    print(num_of_buildings*price)

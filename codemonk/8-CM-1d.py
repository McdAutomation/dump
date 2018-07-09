# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/beautiful-journey-1/description/
N = int(input())
arr = list(map(int,input().split()))
sum = [arr[0]]
for i in range (1,N):
    sum.append(sum[i-1] + arr[i])
total = 0
for i in range(N):
    if sum[i]*(sum[N-1]-sum[i]) > total:
        total = sum[i]*(sum[N-1]-sum[i])
print(total)

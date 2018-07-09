#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/

N = int(input())
arr = list(map(int,input().split(" ")))
ans = 1
for i in range(N):
    ans = (ans * arr[i]) % ( (10**9) + 7 ) 
print(ans)

#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/

l, r, k = tuple(map(int,input().split(" ")))
num = 0
for i in range(l,r+1):
    if i%k == 0:
        num += 1
print(num)

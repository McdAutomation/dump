#https://www.hackerearth.com/challenge/test/programming-practice-challenge/algorithm/c6f4c9b405004de4937dd5e641b1b2f8/
import math
arr = list(map(int,input().split()))
arr.sort()

a = arr[0]
b = arr[1]
count=0
primes = []
#p = [2,3,5,7,11,13,17,19,23,29,31]
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

num = gcd(a,b)

for i in range(1,int(math.sqrt(num))+1):
    if num%i==0:

        if num/i == i:

            count+=1
        else:
            count+=2

print(count)

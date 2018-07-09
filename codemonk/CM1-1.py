#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/prime-number-8/
N = int(input())
primes = []
def is_prime(x):
    size = len(primes)
    flag = 1
    for i in range(size):
        if x%primes[i] == 0:
            flag = 0
            return False
    primes.append(x)
    return True

for i in range(2,N+1):
    if is_prime(i):
        print(i, end=" ")

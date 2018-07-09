#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/magical-word/

T = int(input())
primes = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
size = len(primes)
for t in range(T):
    N = int(input())
    s = input()
    output = []
    for i in range(N):
        x = ord(s[i])
        z = 0
        for z in range(size):
            try:
                if (x >= primes[z]) and (x<=primes[z+1]):
                    break
            except:
                break

        if x <= primes[0]:
            output.append(primes[0])
        elif x >= primes[size-1]:
            output.append(primes[size-1])
        else:
            output.append(primes[z+1] if (primes[z+1] - x) < (x - primes[z]) else primes[z])
    print("".join(list(map(chr,output))))

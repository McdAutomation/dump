#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/
T = int(input())

for t in range(T):
    N = int(input())
    l = 12 * ((N-1)//12) + 1
    r = 12 * (((N-1)//12)+1)
    counter = 0
    while True:
        if (l==N) or (r==N):
            break
        l+=1
        r-=1

    seat = {1:'WS',0:'WS',6:'WS',7:'WS',2:'MS',11:'MS',5:'MS',8:'MS',3:'AS',10:'AS',4:'AS',9:'AS'}

    if l == N:
        print("{} {}".format(r,seat[N%12]))
    elif r == N:
        print("{} {}".format(l,seat[N%12]))

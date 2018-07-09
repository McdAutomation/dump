from sys import stdin,stdout
T = int(stdin.readline())
for t in range(T):
    A, b = tuple(map(int,stdin.readline().split()))
    cur = b
    prev = b
    for i in range(A):
        arr_temp = stdin.readline().split()
        if arr_temp[0]=='P':
            cur, prev = arr_temp[1], cur
        elif arr_temp[0]=='B':
            cur, prev = prev, cur
    stdout.write("Player {}\n".format(cur))

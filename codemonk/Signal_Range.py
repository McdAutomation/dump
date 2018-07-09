from sys import stdin, stdout

T = int(stdin.readline())
for t in range(T):
    N = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    stack = [0]
    ans = [1] * N
    for i in range(1,N):
        while stack and arr[i] > arr[stack[-1]]:
            stack.pop()
        ans[i] = i - stack[-1]
        stack.append(i)
    for i in range(N):
        print(ans[i],end = ' ')

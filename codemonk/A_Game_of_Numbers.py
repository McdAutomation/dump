# https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/a-game-of-numbers-1-5d3a8cb3/
from sys import stdin, stdout

N = int(stdin.readline())
arr = []
for i in range(N):
    arr.append(int(stdin.readline()))

stack = []
stack.append(0)
NGE = [N] * N

for i in range(N):
    index = i
    popped  = stack.pop()
    while True:
        if arr[index] > arr[popped]:
            NGE[popped] = index
            if len(stack) == 0:
                break
            popped = stack.pop()
        else:
            stack.append(popped) # put it back
            break

    stack.append(i)

stack = []
stack.append(0)
NSE = [N] * N
for i in range(N):
    index = i
    popped  = stack.pop()
    while True:
        if arr[index] < arr[popped]:
            NSE[popped] = index
            if len(stack) == 0:
                break
            popped = stack.pop()
        else:
            stack.append(popped) # put it back
            break

    stack.append(i)


for i in range(N):
    try:
        print(arr[NSE[NGE[i]]],end=' ')
    except:
        print(-1,end=' ')

"""
# below is the shortest solution for NGE
stack = []
    for i in range(0, n):
        while stack and arr[stack[-1]] <= arr[n-i-1]: # only sign changes for NSE
            stack.pop()
        if stack:
            max_arr[n-i-1] = stack[-1]
        stack.append(n-i-1)
"""

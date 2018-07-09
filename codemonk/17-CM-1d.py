# https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/a-game-of-numbers-1-5d3a8cb3/description/

from sys import stdin,stdout
N = int(stdin.readline())
arr = []
for i in range(N):
    arr.append(int(stdin.readline()))

print(arr)
nge = [-1]*(N)
stack = []
stack.append(0)
for i in range(1,N):
    next = arr[i]
    index = stack.pop()
    while next > arr[index]:
        nge[index] = i
        if len(stack)==0:
            break
        index = stack.pop()

    if next <= arr[index]:
        stack.append(index)

    stack.append(i)

while len(stack) > 0:
    index = stack.pop()
    nge[index] = -1


nse = [-1]*(N)
stack = []
stack.append(0)
for i in range(N):
    next = arr[i]
    index = stack.pop()
    while next < arr[index]:
        nse[index] = i
        if len(stack)==0:
            break
        index = stack.pop()

    if next > arr[index]:
        stack.append(index)

    stack.append(i)

while len(stack) > 0:
    index = stack.pop()
    nse[index] = -1

print("\n\n\n")
for i in range(N):
    print(arr[nge[i]])

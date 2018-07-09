#https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/monk-and-prisoner-of-azkaban/
from sys import stdin,stdout
N = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
stack = []
new_arr_a = [-1]*(N)

stack.append(0) # first element of array

for i in range(1,N):
    next = arr[i]
    index = stack.pop()
    while next > arr[index]:
        # logic to store index
        new_arr_a[index] = i+1  # 1 indexing
        if len(stack) == 0:
            break
        index = stack.pop()
    if next < arr[index]: # push the element back
        stack.append(index)

    stack.append(i) # also push the current element

while len(stack)>0:
    index = stack.pop()
    new_arr_a[index] = -1


stack_b = []
stack_b.append(N-1)
new_arr_b = [-1]*(N)
for i in range(N-2,-1,-1):
    next = arr[i]
    index = stack_b.pop()
    while next > arr[index] :
        # logic to store index
        new_arr_b[index] = i+1  # 1 indexing
        if len(stack_b) == 0:
            break
        index = stack_b.pop()
    if next < arr[index]: # push the element back
        stack_b.append(index)

    stack_b.append(i) # also push the current element

while len(stack_b)>0:
    index = stack_b.pop()
    new_arr_b[index] = -1

for i in range(N):
    print(new_arr_a[i] + new_arr_b[i],end=" ")

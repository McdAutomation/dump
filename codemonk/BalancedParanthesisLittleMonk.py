# https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/little-monk-and-balanced-parentheses/
from sys import stdin

N = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))

stack = []
count = 0
tempcount = 0
for i in range(N):
    if not stack or arr[i]>0:
        stack.append(arr[i])
    elif stack[-1] == (-1*arr[i]):
        stack.pop()
        count += 2
    else:
        break

print(count)

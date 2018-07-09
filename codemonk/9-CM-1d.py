# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/nice-arches-1/
T = int(input())
count = 0
for t in range(T):
    arr = []
    arr.extend(input())
    N = len(arr)
    j = N
    isBubbly = True
    a = []
    a.append(arr[0])
    for i in range(1,N):
        lenA = len(a)
        if lenA>0 and arr[i] == a[lenA-1]:
            a.pop()
        else:
            a.append(arr[i])
    if len(a) == 0:
        count += 1
print(count)

#https://www.geeksforgeeks.org/magical-indices-array/
input_list = list(map(int,input().split(" ")))

N = len(input_list)
magical = 0
isMagical = True

for i in range(N):
    visited = []
    k = i+1
    isMagical = True
    while isMagical:
        j = ( (k+input_list[k-1]) % N + 1)
        if j-1 not in visited:
            k = j
            visited.append(j-1)
            continue
        else:
            if i in visited:
                magical+=1
            break
print(magical)

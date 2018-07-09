N, Q = tuple(map(int,input().split()))

#arr = list(map(str,input().split()))
arr = []
arr.extend(input().split())
print("".join(arr[0:3]))
binary_values = []
for i in range(N):
    temp = "".join(arr[0:i+1])
    binary_values.append(int(temp,2))
for t in range(Q):
    inp = list(map(int,input().split()))
    if len(inp) == 2:
        print("before->",binary_values)
        print(arr)
        if arr[inp[1]-1] == '1':
            binary_values[inp[1]-1] = binary_values[inp[1]-1] - 2**(inp[1]-1)
        try:
            if arr[inp[1]-1] == '0':
                binary_values[inp[1]-1] = binary_values[inp[1]-2] + 2**(inp[1]-1)
                print("after->",binary_values)
        except:
            binary_values[inp[1]-1] += 2**(inp[1]-1)
    else:
        # str_binary = ""
        # str_binary = "".join(arr[(inp[1]-1):inp[2]])
        sum = binary_values[inp[2]-1] - binary_values[inp[1]-1]
        print(sum)
        print(binary_values)
        if sum%2==0:
            print("EVEN")
        else:
            print("ODD")

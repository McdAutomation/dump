L  = int(input())
T = int(input())
for i in range(T):
    arr = list(map(int,input().split(" ")))
    if (arr[0] < L ) or (arr[1] < L):
        print("UPLOAD ANOTHER")
        continue
    else:
        if arr[0] == arr[1]:
            print("ACCEPTED")
        else:
            print("CROP IT")

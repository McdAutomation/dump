arr = []
arr.extend(input())
size = len(arr)
for i in range(size):
    arr[i] = arr[i].lower() if arr[i].isupper() else arr[i].upper()
print("".join(arr))

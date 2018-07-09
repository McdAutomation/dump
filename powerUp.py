N = int(input())
#arr_input = [1, 2, 1, 2, -2, 5]
arr_input = list(map(int,input().split(" ")))
traversed = []
arr_sum = [-1 for i in range(N)]
largest_sum = 0
largest_of_all = 0
largest_i = 0
for i in range(N):
    for j in range(i,N):
        if arr_input[j] not in traversed:
            largest_sum += arr_input[j]
            if largest_i < largest_sum:
                largest_i = largest_sum
            traversed.append(arr_input[j])
        else:
            responsible = j
            break
    arr_sum[i] = largest_i
    if largest_i > largest_of_all:
        largest_of_all = largest_i
    largest_sum = 0
    largest_i = 0
    traversed = []

    while responsible != -1 and arr_input[i] != arr_input[responsible]:
        i+=1
    responsible = -1

print(largest_of_all)

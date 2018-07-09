T = int(input())
a = [[] for i in range(T)]

for i in range(T):
    list_input = list(input().split(" "))
    size = len(list_input[0])
    R = int(list_input[1])
    iter_j = []
    iter_j.extend(list_input[0])
    for j in range(R):
        temp = []
        for k in range(size):
            if iter_j[k] == '0':
                temp.extend("01")
            else:
                temp.extend("10")
        iter_j = temp[:int(list_input[2])+1]
        size = len(iter_j)
    print(iter_j[int(list_input[2])])
    print(iter_j)

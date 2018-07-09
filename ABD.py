from heapq import *

N = int(input())
N_list = list(map(int,input().split(" ")))

N_list.sort()


Q = int(input())
for i in range(Q):
    s = input()
    s_arr = s.split(" ")
    pos = int(s_arr[0])
    ch = s_arr[1]

    if ch == 'L':
        print(N_list[-pos])
    elif ch == 'S':
        print(N_list[pos-1])

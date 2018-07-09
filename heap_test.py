from heapq import *

class A:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __lt__(self,obj):
        return (self.b>obj.b) or (self.b==obj.b and self.a>obj.a)

hp = []

size = int(input())
for i in range (size):
    st = input()
    ls = list(map(int,st.split(" ")))
    total = ls[2]*50 + ls[3]*5 + ls[4]*10 + ls[5]*20
    diff = total-ls[1]
    print(diff)
    o = A(ls[0],diff,total)
    heappush(hp,o)

for i in range(5):
    print(hp[i].a,hp[i].c)

'''import timeit
from heapq import *
#print(timeit.timeit("print('what is this')",number=1))

ip = [7, 5]
series = [1, 3, 1, 3, 2, 2, 2]
occ = [0 for i in range(ip[0])]
hp = []
class A:
    def __init__(self,s,o,i):
        self.s = s
        self.o = o
        self.i = i
    def __lt__(self,obj):
        return  ((self.o < obj.o) or ((self.o == obj.o) and (self.s < obj.s)))  ##and (self.i <=  obj.i)) #


for i in range(ip[0]):
    occ[series[i]]+=1
    obj = A(series[i],occ[series[i]],i)
    print(series[i],occ[series[i]],"**")
    heappush(hp,obj)
print("\n\n")
for i in range(ip[0]):
    obj = heappop(hp)
    print(obj.s,obj.o)
'''

t_ip = input()
ip = list(map(int,t_ip.split(" ")))

t_series = input()
series = list(map(int,t_series.split(" ")))
occ = [0 for i in range(ip[0])]
hp = []
maxx=0
out = series[0]
j=0
for i in range(ip[0]):
    occ[series[i]]+=1
    if occ[series[i]] > maxx:
        maxx = occ[series[i]]
        out = series[i]
        j=i
    elif occ[series[i]] == maxx:
        if series[i] > series[j]:
            maxx = occ[series[i]]
            out = series[i]
            j=i
    print(out,maxx)

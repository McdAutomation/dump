#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-power-of-time/
from collections import deque
N = int(input())
q = deque(list(map(int,input().split())))
arr = list(map(int,input().split()))
time = 0
for i in range(N):
    while q[0] != arr[i]:
        q.append(q.popleft())
        time+=1
    q.popleft()
    time+=1
print(time)


'''function gradient(startColor, endColor, steps) {
     var start = {
             'Hex'   : startColor,
             'R'     : parseInt(startColor.slice(1,3), 16),
             'G'     : parseInt(startColor.slice(3,5), 16),
             'B'     : parseInt(startColor.slice(5,7), 16)
     }
     var end = {
             'Hex'   : endColor,
             'R'     : parseInt(endColor.slice(1,3), 16),
             'G'     : parseInt(endColor.slice(3,5), 16),
             'B'     : parseInt(endColor.slice(5,7), 16)
     }
     diffR = end['R'] - start['R'];
     diffG = end['G'] - start['G'];
     diffB = end['B'] - start['B'];

     stepsHex  = new Array();
     stepsR    = new Array();
     stepsG    = new Array();
     stepsB    = new Array();

     for(var i = 0; i <= steps; i++) {
             stepsR[i] = start['R'] + ((diffR / steps) * i);
             stepsG[i] = start['G'] + ((diffG / steps) * i);
             stepsB[i] = start['B'] + ((diffB / steps) * i);
             //7-ncolor.length).join(0)
             stepsHex[i] = '#' + Math.round(stepsR[i]).toString(16) + '' + Math.round(stepsG[i]).toString(16) + '' + Math.round(stepsB[i]).toString(16);
     }
     return stepsHex;

 }'''

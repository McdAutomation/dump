n=int(input())
a=list(map(int,input().split()))
b=[0]*n
d={}
k=a[0]
d[a[0]]=0
b[0]=k
index=0
ans=k
for i in range(1,n):
    try:
        c=d[a[i]]
        if c>=index:
            k-=b[c]
            for j in range(i-1,c,-1):
                b[j]-=b[c]
            index=c+1
        d[a[i]]=i
    except:
        d[a[i]]=i
    if a[i]+k>a[i]:
        k=a[i]+k
    else:
        k=a[i]
        index=i
    b[i]=k
    if k>ans:
        ans=k
#print(b)
print(ans)

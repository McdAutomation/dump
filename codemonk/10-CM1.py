T = int(input())
for t in range(T):
    a = {}
    b = {}
    s1,s2 = tuple(input().split())
    size = len(s1)
    for i in range(size):
        try:
            a[s1[i]]+=1
        except:
            a[s1[i]]=1
        try:
            b[s2[i]]+=1
        except:
            b[s2[i]]=1
    if len(a) != len(b):
        print("NO")
    else:
        flag = 1
        for key in a:
            try:
                if a[key] == b[key]:
                    continue
                else:
                    flag = 0
                    break
            except:
                flag = 0
                break
        if flag == 1:
            print("YES")
        else:
            print("NO")

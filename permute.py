N = int(input())
s = []

s.extend(input())
def swap(s,i,j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
print("\n")

def permute(s,start,end):

    if start==end:
        print("".join(s))
    for i in range(start,end+1):
        swap(s,start,i)
        permute(s,start+1,end)
        swap(s,start,i)

permute(s,0,N-1)

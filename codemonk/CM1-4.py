#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/

s = input()
size = len(s)
i = 0
j = size - 1
flag = 1
while i < j:
    if s[i]==s[j]:
        i += 1
        j -= 1
        continue
    else:
        flag = 0
        break

if flag == 1:
    print("YES")
elif flag == 0:
    print("NO")    

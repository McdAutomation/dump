#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/

T = int(input())

for i in range(T):
    str1 = input()
    str2 = input()
    size1 = len(str1)
    size2 = len(str2)
    dict1 = {}
    dict2 = {}
    numOfDeletions = 0
    for i in range(size1):
        try:
            dict1[str1[i]]+=1
        except:
            dict1[str1[i]] = 1
    for i in range(size2):
        try:
            dict2[str2[i]]+=1
        except:
            dict2[str2[i]] = 1
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    set3 = set1 & set2
    set4 = set1 ^ set2
    for key in set3:
        diff = dict1[key] - dict2[key]
        numOfDeletions += diff if diff>0 else -diff
    for key in set4:
        try:
            numOfDeletions += dict1[key]
        except:
            pass
        try:
            numOfDeletions += dict2[key]
        except:
            pass


    print(numOfDeletions)

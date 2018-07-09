#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/minimise-cost-89b54cb9/

list_input = []
list_input.extend(input())
t_c = int(input())
t_i = t_c
t_i = t_i % 10
t_c = t_c % 26
size = len(list_input)
encoded = []
for i in range(size):
    t = ord(list_input[i])
    if (t >= 65) and (t <= (90-t_c)):
        encoded.append(chr(t+t_c))
    elif (t>(90-t_c)) and t<=90:
        encoded.append(chr(65+t%(90-t_c) - 1))

    elif (t >= 97) and (t <= (122-t_c)):
        encoded.append(chr(t+t_c))
    elif (t>(122-t_c)) and t<=122:
        encoded.append(chr(97+t%(122-t_c) - 1))

    elif (t >= 48) and (t <= (57-t_i)):
        encoded.append(chr(t+t_i))
    elif (t>(57-t_i)) and t<=57:
        encoded.append(chr(48+t%(57-t_i) -1))

    else:
        encoded.append(list_input[i])
print("".join(encoded))

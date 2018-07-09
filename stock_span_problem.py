def calculateSpan(arr,s):
    size = len(price)
    stack = []
    stack.append(0)
    s[0] = 1
    for i in range(1,size):
        while(len(stack)>0 and arr[stack[len(stack)-1]] < arr[i]):
            stack.pop()
        if len(stack) > 0:
            s[i] = i - stack[len(stack)-1] 
        else:
            s[i] = i + 1
        stack.append(i)
    print(s)


# Driver program to test above function
price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price)+1)]

# Fill the span values in array S[]
calculateSpan(price, S)

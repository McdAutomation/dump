# https://www.geeksforgeeks.org/next-greater-element/

def printNGE(arr):
    stack = []
    stack.append(arr[0])
    for i in range(len(arr)):
        if len(stack) > 0:
            next = arr[i]
            popped = stack.pop()
            while next > popped:
                print("{}----{}".format(popped,next))
                if len(stack) == 0:
                    break
                popped = stack.pop()

            if next < popped:
                stack.append(popped)
        stack.append(arr[i])

    while len(stack) >0:
        print("{}   ----   {}".format(popped,-1))
        popped = stack.pop()

arr = [11, 13, 21, 3]
printNGE(arr)

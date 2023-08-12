def getMax(operations):
    # Write your code here
    stack = [0]
    res = []
    for i in operations:
        i = i.split()
        if i[0] == '1':
            stack.append(max(int(i[1]),int(stack[-1])))
        elif i[0] == '2':
            stack.pop()
        else:
            res.append(stack[-1])
    return res

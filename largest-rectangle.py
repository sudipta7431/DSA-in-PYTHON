def largestRectangle(h):
    # Write your code here
    index = area = 0
    stack = []
    h.append(0)
    while(index < len(h)):
        if not stack or h[stack[-1]] < h[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = max(area, h[top] * (index - stack[-1] -1 if stack else index))
    return area

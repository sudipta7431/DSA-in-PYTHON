def twoStacks(maxSum, a, b):
    # Write your code here
    temp = count = i = j = 0 
    while i < len(a) and temp + a[i] <= maxSum:
        temp += a[i]
        i += 1
        count += 1
    while j < len(b) and i >= 0:
        temp += b[j]
        j += 1
        while i > 0 and temp > maxSum:
            i -= 1
            temp -= a[i]
        if temp <= maxSum and count < i+j:
            count = i+j
    return count

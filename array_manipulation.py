#FIRST LOGIC BUT TIME COMPLAXCITY IS HIGH
def arrayManipulation(n, queries):
    # Write your code here
    l = [0] * n
    a = 0
    m = len(queries)
    
    
    for i in range(m):
        low = queries[i][0]
        high = queries[i][1]
        iteam = queries[i][2]
        for j in range(low,high+1):
            l[j-1] = l[j-1] + iteam
    
    return max(l)

#FINAL BEST ALGO
def arrayManipulation(n, queries):
    # Write your code here
    l = [0]*(n+2)
    for a,b,k in queries:
        l[a] += k
        l[b+1] -= k  
    maxnum = temp = 0
    for val in l:
        temp += val
        maxnum = max(maxnum,temp)
    return maxnum

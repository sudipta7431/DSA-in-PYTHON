def equalStacks(h1, h2, h3):
    # Write your code here
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)
    while(h1 and h2 and h3):
        if s1 == s2 == s3:
            return s1
        else:
            if (s1 > s2) or (s1 > s3):
                s1 -= h1.pop(0)
            elif (s2 > s1) or (s2 > s3):
                s2 -= h2.pop(0)
            elif (s3 > s2) or (s3 > s1):
                s3 -= h3.pop(0)
    return 0

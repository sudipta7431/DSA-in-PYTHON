ab = 'racecar'
def check_Palindrome(x):
    final = []
    n = len(x)
    for i in range(1, n+1):
        final.append(x[n-i])
    a1 = conv(final)
    return a1

def conv(z):
    a = ""
    for element in z:
        a += element
    return a

def check(b):
    d = b
    a = check_Palindrome(d)
    if a == d:
        print(True)
    else:
        print(False)

check(ab)


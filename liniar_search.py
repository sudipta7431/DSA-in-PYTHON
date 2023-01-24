def linear(arr,k):
    posi = 0
    fla = 0
    for i in arr:
        if i == k:
            posi = posi + 1
            fla = 1
            break
        else:
            posi = posi + 1
            fla = 0
    if fla == 1:
        return posi
    else:
        return -1
arr = list(map(int,input("Enter the numbers : ").strip().split(",")))
k = int(input("Enter the Data You want Search : "))
posi = linear(arr,k)
if posi == -1:
    print("Not Present")
else:
    print("DATA " + str(k) + " --> PRESENT IN POSITION " + str(posi))
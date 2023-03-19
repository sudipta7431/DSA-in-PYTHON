def reverse(llist):
    # Write your code here
    prv = None
    cur = llist
    nxt = llist.next
    
    while(cur != None):
        nxt = cur.next
        cur.next = prv
        cur.prev = nxt
        prv = cur
        cur = nxt
    llist = prv
    return llist
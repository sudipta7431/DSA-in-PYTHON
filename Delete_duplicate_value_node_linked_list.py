#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def removeDuplicates(llist):
    # Write your code here
    new_list = SinglyLinkedList()
    a = []
    while llist:
        if llist.data not in a:
            a.append(llist.data)
        llist = llist.next
    for i in a:
        new_list.insert_node(i)
        
    return new_list.head
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sortedInsert(llist, data):
    # Write your code here   
    node = DoublyLinkedListNode(data)
    if llist == None:
        llist = node
    elif data < llist.data:
        node.next = llist
        llist.prev = node
        llist = node
    else:
        cureent = llist
        while cureent.next != None and cureent.data < data:
            cureent = cureent.next
        if cureent.next == None and cureent.data < data:
            cureent.next = node
            node.prev = cureent
        else:
            privious = cureent.prev
            privious.next = node
            node.prev = privious
            node.next = cureent
            cureent.prev = node
        
    return llist
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
#!/usr/bin/env python

import math
from LinkedList import *

class Entry:
    """ Entry

        Used in every hashtable but the ChainedHashtable, an Entry is a key, value pair
    """

    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value

class Link:
    """ Link

        Used in the ChainedHashtable, a Link is a key, value pair for use in a linked list.
    """
    def __init__(self, key = 0, value = 0, next = None):
        self.key = key
        self.value = value
        self.next = next

def DivisionHash(key, size):
    return key % size

def AuxiliaryHash(key, size):
    A = 0.618
    return math.floor(size * ((key * A) % 1))

def LinearHash(key, i, size):
    return (AuxiliaryHash(key, size) + i) % size

def AuxiliaryHash2(key, size):
    return 1 + (key % size - 1)

def QuadraticHash(key, i, size):
    c_1 = 0.5
    c_2 = 0.5
    return (AuxiliaryHash(key, size) + c_1 * i + c_2 * i * i) % size

def DoubleHash(key, i, size):
    return (DivisionHash(key, size) + i * AuxiliaryHash2(key, size)) % size

class ChainedHashtable:
    """ Chained Hashtable
    
        A linked list of Keys and Values are stored in the links array, which holds a linked list of all the mapped values
    """

    size = 23

    def put(self, key, value):
        llist = self.links[self.hash(key)]
        if llist == None:
            node = Node(key = key, value = value)
            llist = LinkedList(head=node)
            return
        cur_node = llist.head
        while cur_node != None:
            if cur_node.key == key:
                cur_node.value = value
                return
            else:
                cur_node = cur_node.next
        llist.push(Node(key = key, value = value))

    def get(self, key):
        llist = self.links[self.hash(key)]
        if llist == None:
            return None
        cur_node = llist.head
        while cur_node != None:
            if cur_node.key = key:
                return cur_node.value
            else:
                cur_node = cur_node.next
        return None
    
    def hash(self, key):
        return DivisionHash(key,size)

    def __init__(self):
        self.links = [None] * size

def LinearHashtable:
    """ Linear Hashtable
        
        Keys and Values are stored in an associative array, and probed for values by searching linearly through the table
    """
    size = 32

    def get(self, key):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry == None or entry.key != key):
            i+=1
            if i == size:
                return None
            entry = self.entries[self.hash(key, i)]
        return entry.value

    def put(self, key, value):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry != None and entry.key != key):
            i+=1
            if i == size:
                raise Exception("Table is Full!")
                return
            entry = self.entries[self.hash(key, i)]
        if entry == None:
            entry = Entry(key = key, value = value)
        else:
            entry.value = value

    def hash(self, key, i):
        return LinearHash(key, i, size)
    
    def __init__(self):
        self.entries = [None] * size


def QuadraticHashtable:
    """ Quadratic Hashtable

        Keys and Values are stored in an associative array, and probed for values by searching quadratically through the table
    """
    size = 32

    def get(self, key):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry == None or entry.key != key):
            i+=1
            if i == size:
                return None
            entry = self.entries[self.hash(key, i)]
        return entry.value

    def put(self, key, value):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry != None and entry.key != key):
            i+=1
            if i == size:
                raise Exception("Table is Full!")
                return
            entry = self.entries[self.hash(key, i)]
        if entry == None:
            entry = Entry(key = key, value = value)
        else:
            entry.value = value
    
    def hash(self, key, i):
        return QuadraticHash(key, i, size)

    def __init__(self):
        self.entries = [None] * size

def DoubleHashtable:
    """ Double Hashtable

        Keys and Values are stored in an associative array, and probed for values by searching with a double hashing probing sequence
    """
    size = 31

    def get(self, key):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry == None or entry.key != key):
            i+=1
            if i == size:
                return None
            entry = self.entries[self.hash(key, i)]
        return entry.value

    def put(self, key, value):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry != None and entry.key != key):
            i+=1
            if i == size:
                raise Exception("Table is Full!")
                return
            entry = self.entries[self.hash(key, i)]
        if entry == None:
            entry = Entry(key = key, value = value)
        else:
            entry.value = value

    def hash(self, key, i):
        return DoubleHash(key, i, size)

    def __init__(self):
        self.entries = [None] * size


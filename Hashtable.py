#!/usr/bin/env python

import math
from LinkedList import *

class Entry:
    """ Entry

        Used in every hashtable but the ChainedHashtable, an Entry is a key, value pair
    """

    def __str__(self):
        return str(self.value)

    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value

class Link:
    """ Link

        Used in the ChainedHashtable, a Link is a key, value pair for use in a linked list.
    """

    def __str__(self):
        if self.next == None:
            return str(self.value) + " "
        else:
            return str(self.value) + " " + str(self.next)

    def __init__(self, key = 0, value = 0, next = None):
        self.key = key
        self.value = value
        self.next = next

def DivisionHash(key, size):
    return key % size

def AuxiliaryHash(key, size):
    A = 0.618
    return int(math.floor(size * ((key * A) % 1)))

def LinearHash(key, i, size):
    return (AuxiliaryHash(key, size) + i) % size

def AuxiliaryHash2(key, size):
    return 1 + (key % (size - 1))

def QuadraticHash(key, i, size):
    c_1 = 0.5
    c_2 = 0.5
    return int((AuxiliaryHash(key, size) + c_1 * i + c_2 * i * i) % size)

def DoubleHash(key, i, size):
    return int((DivisionHash(key, size) + i * AuxiliaryHash2(key, size)) % size)

class ChainedHashtable:
    """ Chained Hashtable
    
        A linked list of Keys and Values are stored in the links array, which holds a linked list of all the mapped values
    """

    Size = 23

    def put(self, key, value):
        llist = self.links[self.hash(key)]
        if llist == None:
            node = Link(key = key, value = value)
            llist = LinkedList(head=node)
            self.links[self.hash(key)] = llist
            return
        cur_node = llist.head
        while cur_node != None:
            if cur_node.key == key:
                cur_node.value = value
                return
            else:
                cur_node = cur_node.next
        llist.push(Link(key = key, value = value))

    def get(self, key):
        llist = self.links[self.hash(key)]
        if llist == None:
            return None
        cur_node = llist.head
        while cur_node != None:
            if cur_node.key == key:
                return cur_node.value
            else:
                cur_node = cur_node.next
        return None
    
    def search(self, key):
        llist = self.links[self.hash(key)]
        if llist == None:
            return str(self.hash(key))
        search_result = ""
        cur_node = llist.head
        search_result += str(self.hash(key)) + " " 
        while cur_node != None:
            search_result += str(cur_node.value) + " "
            if cur_node.key == key:
                return search_result
            else:
                cur_node = cur_node.next
        return search_result


    def insert(self, value):
        self.put(value, value)

    def hash(self, key):
        return DivisionHash(key, ChainedHashtable.Size)

    def __str__(self):
        lines = []
        for i in range(len(self.links)):
            lines.append("" + str(i) + "\t" + ("" if self.links[i] == None else str(self.links[i])))
        return "\n".join(lines)

    def __init__(self):
        self.links = [None] * ChainedHashtable.Size

class LinearHashtable:
    """ Linear Hashtable
        
        Keys and Values are stored in an associative array, and probed for values by searching linearly through the table
    """
    Size = 32

    def get(self, key):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry == None or entry.key != key):
            i+=1
            if i == LinearHashtable.Size:
                return None
            entry = self.entries[self.hash(key, i)]
        return entry.value

    def search(self, key):
        i = 0
        search_result = ""
        entry = self.entries[self.hash(key, i)]
        search_result = str(self.hash(key, i)) + " "
        while (entry == None or entry.key != key):
            i+=1
            if i == LinearHashtable.Size:
                return search_result + "-1"
            entry = self.entries[self.hash(key, i)]
            search_result += str(self.hash(key, i)) + " "
        return search_result

    def put(self, key, value):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry != None and entry.key != key):
            i+=1
            if i == LinearHashtable.Size:
                #raise Exception("Table is Full!")
                return
            entry = self.entries[self.hash(key, i)]
        if entry == None:
            entry = Entry(key = key, value = value)
            self.entries[self.hash(key, i)] = entry
        else:
            entry.value = value
    
    def insert(self, value):
        self.put(value, value)

    def hash(self, key, i):
        return LinearHash(key, i, LinearHashtable.Size)

    def __str__(self):
        lines = []
        for i in range(len(self.entries)):
            lines.append("" + str(i) + "\t" + ("-1" if self.entries[i] == None else str(self.entries[i].value)))
        return "\n".join(lines)
    
    def __init__(self):
        self.entries = [None] * LinearHashtable.Size


class QuadraticHashtable:
    """ Quadratic Hashtable

        Keys and Values are stored in an associative array, and probed for values by searching quadratically through the table
    """
    Size = 32

    def get(self, key):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry == None or entry.key != key):
            i+=1
            if i == QuadraticHashtable.Size:
                return None
            entry = self.entries[self.hash(key, i)]
        return entry.value

    def put(self, key, value):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry != None and entry.key != key):
            i+=1
            if i == LinearHashtable.Size:
                #raise Exception("Table is Full!")
                return
            entry = self.entries[self.hash(key, i)]
        if entry == None:
            entry = Entry(key = key, value = value)
            self.entries[self.hash(key, i)] = entry
        else:
            entry.value = value

    def search(self, key):
        i = 0
        search_result = ""
        entry = self.entries[self.hash(key, i)]
        search_result = str(self.hash(key, i)) + " "
        while (entry == None or entry.key != key):
            i+=1
            if i == LinearHashtable.Size:
                return search_result + "-1"
            entry = self.entries[self.hash(key, i)]
            search_result += str(self.hash(key, i)) + " "
        return search_result
    
    def hash(self, key, i):
        return QuadraticHash(key, i, QuadraticHashtable.Size)

    def insert(self, value):
        self.put(value, value)

    def __str__(self):
        lines = []
        for i in range(len(self.entries)):
            lines.append("" + str(i) + "\t" + ("-1" if self.entries[i] == None else str(self.entries[i].value)))
        return "\n".join(lines)

    def __init__(self):
        self.entries = [None] * QuadraticHashtable.Size

class DoubleHashtable:
    """ Double Hashtable

        Keys and Values are stored in an associative array, and probed for values by searching with a double hashing probing sequence
    """
    Size = 31

    def get(self, key):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry == None or entry.key != key):
            i+=1
            if i == DoubleHashtable.Size:
                return None
            entry = self.entries[self.hash(key, i)]
        return entry.value

    def put(self, key, value):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while (entry != None and entry.key != key):
            i+=1
            if i+1 == LinearHashtable.Size:
                #raise Exception("Table is Full!")
                return
            entry = self.entries[self.hash(key, i)]
        if entry == None:
            entry = Entry(key = key, value = value)
            self.entries[self.hash(key, i)] = entry
        else:
            entry.value = value

    def search(self, key):
        i = 0
        search_result = ""
        entry = self.entries[self.hash(key, i)]
        search_result = str(self.hash(key, i)) + " "
        while (entry == None or entry.key != key):
            i+=1
            if i+1 == LinearHashtable.Size:
                return search_result + "-1"
            entry = self.entries[self.hash(key, i)]
            search_result += str(self.hash(key, i)) + " "
        return search_result

    def insert(self, value):
        self.put(value, value)

    def hash(self, key, i):
        return DoubleHash(key, i, DoubleHashtable.Size)

    def __str__(self):
        lines = []
        for i in range(len(self.entries)):
            lines.append("" + str(i) + "\t" + ("-1" if self.entries[i] == None else str(self.entries[i].value)))
        return "\n".join(lines)

    def __init__(self):
        self.entries = [None] * DoubleHashtable.Size


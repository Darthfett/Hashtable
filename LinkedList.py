class LinkedList:

    def push(self, new, prev = None):
        if prev == None:
            new.next = self.head
            self.head = new
        else:
            new.next = prev.next
            prev.next = new

    def pop(self, index = 0):
        cur = index
        prev_node = None
        cur_node = self.head
        while cur > 0:
            prev_node = cur_node
            cur_node = cur_node.next
            cur -= 1
            
        if prev_node == None:
            popped = self.head
            self.head = self.head.next
            return popped
        else:
            prev_node = cur_node.next
            return cur_node

    def insert(self, node, index = 0):
        if node == None:
            raise Exception("node is None Type")
            return
        cur = index
        prev_node = None
        cur_node = self.head
        while cur > 0:
            prev_node = cur_node
            cur_node = cur_node.next
            cur -= 1

        if prev_node == None:
            self.head = node
        else:
            prev_node.next = node

        node.next = cur_node

    def __str__(self):
        if self.head == None:
            return ""
        else:
            return str(self.head)

    def __init__(self, head = None):
        self.head = head

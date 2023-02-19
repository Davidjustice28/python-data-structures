# implements a linked list class - methods: append, prepend, includes, length, pop, shift, remove, reverse

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __str__(self) -> str:
        #return "value: {}, next => {}".format(self.value,self.next)
        return "{}".format(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def __str__(self) -> str:
        string = ""
        n = self.head
        while(n is not None):
            string += n.value
            n = n.next
            if(n is not None):
                string += " => "
        return string
    
    @classmethod
    def make_list(cls):
        return cls()
    

    def append(self,value):
        self.length += 1

        def loop_list(node):
            if(self.head is None):
                self.head = Node(value)
                print("Node added")
                return
            elif(node.next is None):
                node.next = Node(value)
                print("Node added")
            else:
                return loop_list(node.next)
                

        loop_list(self.head)


    def prepend(self,value):
        self.length +=1
        next = self.head
        new_head = Node(value)
        self.head = new_head
        self.head.next = next
        print("Node added")


    def includes(self,value):
        node = self.head
        found_value = False
        while(node is not None):
            if(node.value == value):
                found_value = True
            node = node.next
        return found_value
    
    
    def pop(self):
        current_node = self.head
        prev_node = None
        while(current_node is not None):
            if current_node.next is None:
                prev_node.next = None
                self.length -= 1
                return current_node
            else:
                prev_node = current_node
                current_node = current_node.next


    def shift(self):
        if(self.head and (self.head.next is not None)):
            new_head = self.head.next
            prev_head = self.head
            self.head = new_head
            self.length -= 1
            return prev_head
        
        
    def remove(self,value):
        node = self.head
        prev = None
        while node is not None:
            if node.value == value :
                if prev is None:
                    self.head = None
                else:
                    prev.next = None
                print("an item was removed from your list")
                self.length -= 1
                return
            else:
                prev = node
                node = node.next
        print("no item found in list to remove")

    def reverse(self):
        new_order = []
        node = self.head
        while node is not None:
            new_order.insert(0,node)
            node = node.next
        new_list = self.make_list()
        for n in new_order:
            new_list.append(n.value)
        return new_list
    


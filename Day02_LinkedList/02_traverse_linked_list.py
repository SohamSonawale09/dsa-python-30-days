# Traverse from head
# Print each node’s data 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
         self.head = None
        
    def insert_at_bigning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")
        
        
L1 = LinkedList()
L1.insert_at_bigning(10)
L1.insert_at_bigning(20)
L1.insert_at_bigning(30)
L1.insert_at_end(40)
L1.print_list() 
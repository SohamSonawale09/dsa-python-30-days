# 1 create_linked_list.py

# Node class

# Create 3-4 nodes

# Link them Print head value 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linklist:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def print_lst(self):
        temp = self.head
        while temp:
            print(temp.data,end ="->")
            temp = temp.next 
        print("None") 
        
l1= Linklist()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.print_lst()
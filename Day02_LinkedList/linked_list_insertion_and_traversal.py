class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linklist:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
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
        
l1 = Linklist()
l1.insert_at_begining(10)
l1.insert_at_begining(20)
l1.insert_at_begining(30)
l1.insert_at_end(9)
l1.print_list()
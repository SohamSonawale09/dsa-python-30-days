class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linklist():
    def __init__(self):
        self.head = None
    
    
    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
    
    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

            
c = Linklist()
c.insert(10)
c.insert(20)
c.insert(30)
c.show()
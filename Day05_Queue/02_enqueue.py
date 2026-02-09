# Q2 Enqueue operation

# Add elements to queue
queue = []
# Print queue after each insert 
def add_in_queue(a):
    queue.append(a)
    print (queue)
    
while True:
    a = int(input("Enter number (-1 to stop):"))
    if a == -1:
        break
    add_in_queue(a)

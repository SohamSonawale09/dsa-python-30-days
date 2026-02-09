# Q3 Dequeue operation
# Remove element from front
# Handle empty queue case

queue = [1, 3, 5, 6, 7, 8]

if not queue:
    print("Queue is empty")
else:
    removed = queue.pop(0)
    print("Removed element:", removed)
    print("Queue after dequeue:", queue)

from collections import deque

# Queue = FIFO (First In First Out)

queue = deque()

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print("Queue:", queue)

# dequeue
queue.popleft()

print("After dequeue:", queue)

# When to use Queue:
# - BFS Traversal
# - Scheduling tasks
# - Level order traversal in trees

print("Queue Revision Completed ✅")
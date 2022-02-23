# Queue (FIFO queue)

Q = [None] * 100
Front = 0
Back = 0

# next
def next(Q: list, p: int):
  p = p + 1    
  if p == len(Q):
    p = 0
  return p

# is_empty
def is_empty(Front: int, Back: int):
  return Front == Back

# is_full
def is_full(Q: list, Front: int, Back: int):
  return next(Back) == Front

# enqueue
def enqueue(Q: list, Front: int, Back: int, x):
  if is_full(Q, Front, Back):
    print("Queue is full.")
  else:
    Q[Back] = x
    Back = next(Back)

# dequeue
def dequeue(Q: list, Front: int, Back: int):
  if is_empty(Q, Front, Back):
    print("Queue is empty.")
  else:
    x = Q[Front]
    Front = next(Front)
    return x
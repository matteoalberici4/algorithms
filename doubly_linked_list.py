# Doubly Linked List

class list_element:
  def __init__(self, value, n, previous):
    self.value = value
    self.n = n
    self.previous = previous

L = list_element()
L.next = L
L.previous = L

# print_all
def print_all():
  x = L.next
  while x != L:
    print(x.value)
    x = x.next

# insert_after
def insert_after(x: list_element, value: int):
  n = list_element()
  n.value = value
  n.prev = x
  n.next = x.next
  n.prev.next = n
  n.next.prev = n

# insert_before
def insert_before(x: list_element, value: int):
  n = list_element()
  n.value = value
  n.prev = x.prev
  n.next = x
  n.prev.next = n
  n.next.prev = n

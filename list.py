# List

class list_element:
  def __init__(self, value, n):
    self.value = value
    self.next = n

# insert_after
def insert_after(x: list_element, value: int):
  x.next = list_element(value, x.next)

# find
def find(L: list_element, value: int):
  l = L
  while l != None:
    if value == l.value:
      return True
    i -= 1
    l = l.next
  return False

# get_element_at
def get_element_at(L: list_element, i: int):
  l = L
  while l != None:
    if i == 0:
      return l.value
    i -= 1
    l = l.next
  print("Index out of bounds.")

# is_empty
def is_empty(L: list_element):
  return L == None

# insert_front
def insert_front(L: list_element, value: int):
  L = list_element(value, L)

# pop_front
def pop_front(L: list_element,):
  if L == None:
    print("List is empty")
  else:
    v = L.value
    L = L.next
    return v

# print_all
def print_all(L: list_element,):
  l = L
  while l != None:
    print(l.value)
    l = l.next

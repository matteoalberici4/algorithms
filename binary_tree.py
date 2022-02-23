# Binary Search Tree

class Node:
  def __init__(self, value):
    self.key = value
    self.left = None
    self.right = None
    self.parent = None

T = Node(12)
T.left = Node(5)
T.right = Node(18)
T.left.left = Node(2)
T.right.left = Node(15)

# print_in_order
def bst_print_in_order(T: Node):
  if T != None:
    bst_print_in_order(T.left)
    print(T.key)
    bst_print_in_order(T.right)

# bst_size
def bst_size(T: Node):
  if T == 0:
    return 0
  return bst_size(T.left) + 1 + bst_size(T.right)

# bst_height
def bst_height(T: Node):
  if T == None:
    return 0
  return 1 + max(bst_height(T.left), bst_height(T.right))

# bst_min
def bst_min(T: Node):
  if T == None:
    return None
  while T.left != None:
    T = T.left
  return T

# bst_max
def bst_max(T: Node):
  if T == None:
    return None
  while T.right != None:
    T = T.right
  return T

# bst_next
def bst_next(T: Node):
  if T.right != None:
    return bst_min(T.right)
  P = T.parent
  while P != None and P.left != T:
    T = P
    P = P.parent
  return P

# bst_previous
def bst_previous(T: Node):
  if T.left != None:
    return bst_max(T.left)
  P = T.parent
  while P != None and P.right != T:
    T = P
    P = P.parent
  return P

# bst_search
def bst_search(T: Node, k: int):
  while T != None and T.key != k:
    if k > T.key:
      T = T.right
    else:
      T = T.left
  return T != None

# bst_insert
def bst_insert(T: Node, Z: Node):
  Y = None
  X = T
  while X != None:
    Y = X
    if Z.key < X.key:
      X = X.left
    else:
      X = X.right
  Z.parent = Y
  if Y == None:
    T = Z
  else:
    if Z.key < Y.key:
      Y.left = Z
    else:
      Y.right = Z
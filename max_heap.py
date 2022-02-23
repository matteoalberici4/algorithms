# Max heap

# heapify
def heapify(H: list):
  for i in range(len(H)):
    insert_helper(H, 0, i)

# max_heap_insert
def max_heap_insert(H: list, key: int):
  H.append(key)
  insert_helper(H, 0, len(H) - 1)

# insert_helper
def insert_helper(H: list, begin: int, end: int):
  if end == begin or end == 0:
    return
  if H[parent(end)] < H[end]:
    H[parent(end)], H[end] = H[end], H[parent(end)]
    insert_helper(H, begin, parent(end))
  else:
    return

# extract_max
def extract_max(H: list):
  m = H[0]
  H[0], H[len(H) - 1] = H[len(H) - 1], H[0]
  H.pop()
  reorder_root(H, 0, len(H) - 1)
  return m

# heap_sort
def heap_sort(H: list):
  for j in range(len(H) - 1, 0, -1):
    H[0], H[j] = H[j], H[0]
    reorder_root(H, 0, j - 1)

# reorder_root
def reorder_root(H: list, begin: int, end: int):
  if 2 * begin + 2 > end:
    if 2 * begin + 1 > end: 
      return
    else:
      l = left(begin)
      if H[l] > H[begin]:
        H[begin], H[l] = H[l], H[begin]
      return
  l = left(begin)
  r = right(begin)
  if H[l] > H[begin] or H[r] > H[begin]:
    if H[l] > H[r]:
      H[begin], H[l] = H[l], H[begin]
      reorder_root(H, l, end)
    else:
      H[begin], H[r] = H[r], H[begin]
      reorder_root(H, r, end)

# parent
def parent(i: int):
  return (i - 1) // 2 

# left
def left(i: int):
  return i * 2 + 1

# right
def right(i: int):
  return i * 2 + 2

# is_heap
def is_heap(H: list, i: int):
  if 2 * i + 2 > len(H):
    return True
  l = True
  r = True
  if H[i] >= H[left(i)]:
    l = is_heap(H, left(i))
  else:
    l = False    
  if right(i) < len(H):
    if H[i] >= H[right(i)]:
      r = is_heap(H, right(i))
    else:
      r = False
  return l and r
# Binary search

def binary_search(A: list, x: int):
  i = 0
  j = len(A)
  while i < j:
    m = (i + j) // 2
    if A[m] == x:
      return True
    elif A[m] > x:
      j = m
    else: 
      i = m + 1
  return False

def recursive_binary_search(A: list, x: int, start: int, end: int):
  if end >= start:
    m = start + (end - start) // 2
    if A[m] == x:
      return m
    elif A[m] > m:
      return recursive_binary_search(A, start, m - 1, x)
    else:
      return recursive_binary_search(A, m + 1, end, x)
  else:
    return -1
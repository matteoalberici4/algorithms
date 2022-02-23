# Merge sort

def merge(A: list, B: list):
  i = 0       
  j = 0                    
  X = []
  while i < len(A) or j < len(B):
    if i < len(A) and (j >= len(B) or A[i] <= B[j]):
      X.append(A[i])
      i = i + 1
    else:
      X.append(B[j])
      j = j + 1
  return X

def merge_sort(A: list, begin: int, end: int):
  if end - begin == 1:
    return [A[begin]]
  elif end - begin == 0:
    return []
  m = (begin + end) // 2
  L = merge_sort(A, begin, m)
  R = merge_sort(A, m, end)
  return merge(L, R)
    
# Complexity:
#   worst-case: Θ(nlogn)
#   best-case: Θ(nlogn)
#   average-case: Θ(nlogn)
#   in-place: no
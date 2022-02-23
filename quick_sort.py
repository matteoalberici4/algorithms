# Quick sort

def partition(A: list, begin: int, end: int):
  assert end - begin > 1
  pivot = A[end - 1]
  q = begin
  for i in range(begin, end - 1):
    if A[i] < pivot:
      A[i], A[q] = A[q], A[i]
      q += 1
  A[end - 1], A[q] = A[q], A[end - 1]
  return q

def quick_sort(A: list, begin: int, end: int):
  if end - begin >= 2:
    q = partition(A, begin, end)
    quick_sort(A, begin, q)
    quick_sort(A, q + 1, end)

# Complexity:
#   worst-case: Θ(n^2)
#   best-case: Θ(nlogn)
#   average-case: Θ(nlogn)
#   in-place: yes
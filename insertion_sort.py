# Insertion sort

def insertion_sort(A: list):
  for i in range(1, len(A)):
    j = i
    while j > 0 and A[j - 1] > A[j]:
      A[j], A[j - 1] = A[j - 1], A[j]
      j -= 1

# Complexity:
#   worst-case: Θ(n^2)
#   best-case: Θ(n)
#   average-case: Θ(n^2)
#   in-place: yes

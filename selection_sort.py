# Selection sort

def selection_sort(A: list):
  for i in range(0, len(A) - 1):
    for j in range(i + 1, len(A)):
      if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]

# Complexity:
#   worst-case: Θ(n^2)
#   best-case: Θ(n^2)
#   average-case: Θ(n^2)
#   in-place: yes
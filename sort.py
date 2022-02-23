# Basic sorting

def sorting(A: list):
  for i in range(len(A)):
    for j in range(len(A)):
      if A[j] < A[i]:
        A[i], A[j] = A[j], A[i]
# Bubble sort

def bubble_sort(Array: list):
  while True:
    changes = 0
    for index in range(len(Array) - 1):
      if Array[index] > Array[index + 1]:
        Array[index], Array[index + 1] = Array[index + 1], Array[index]
        changes = changes + 1
    if changes == 0:
      return Array

# Complexity:
#   worst-case: Θ(n^2)
#   best-case: Θ(n^2)
#   average-case: Θ(n^2)
#   in-place: yes
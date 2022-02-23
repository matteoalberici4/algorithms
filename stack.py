# Stack (LIFO queue)

S = [None] * 100
N = 0

# push
def push(S: list, N: int, x: int):    
  if N < len(S):
    S[N] = x
    N = N + 1
  else:
      print("Stack overflow.")

# pop
def pop(S: list, N: int):    
  if N > 0:
    N = N - 1
    return S[N]
  print("Stack underflow.")

# is_empyty
def is_empty(N: int):
  return N == 0
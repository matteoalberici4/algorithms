# Breadth-First Search

import sys

def bfs():
  V = []    # vertexes 
  Adj = []    # adjacency list
  V_idx = {}    # index: name --> vertex_id
  for line in sys.stdin:
    A = line.strip().split()
    for v in A:
      if not v in V_idx:    # v is a string (vertex name)
        V_idx[v] = len(V)
        V.append(v)
        Adj.append([])
    v_i = V_idx[A[0]]
    for i in range(1,len(A)):
      u_i = V_idx[A[i]]
      Adj[u_i].append(v_i)
      Adj[v_i].append(u_i)
  n = len(V)
  Visited = [False] * n
  Q = [0]
  head = 0
  Visited[0] = True
  count = 1
  while head < len(Q):
    v = Q[head]
    head += 1
    for u in Adj[v]:
      if not Visited[u]:
        Visited[u] = True
        Q.append(u)
        count += 1
  if count == n:
    print('connected')
  else:
    print('disconnected')
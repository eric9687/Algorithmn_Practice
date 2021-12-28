##1753
# import sys
# from heapq import *
# input = sys.stdin.readline

# n,m = map(int,input().split())
# st = int(input())
# adj = [[] for _ in range(n+1)]

# for _ in range(m):
#     a,b,c = map(int, input().split())
#     adj[a].append((b,c))

# INF = int(1e9) + 7
# dist = [INF]* (n+1)
# dist[st] = 0
# PQ = [(dist[st],st)]

# while PQ:
#     cdist ,cur = heappop(PQ)
#     if dist[cur] != cdist: continue
#     for nxt,cost in adj[cur]:
#         if dist[nxt] > dist[cur] + cost:
#             dist[nxt] = dist[cur] + cost
#             heappush(PQ,(dist[nxt],nxt))
            
# for i in range(1,n+1):
#     print(INF if dist[i] == INF else dist[i])
    
## 1260 dfs & bfs

# import sys
# input = sys.stdin.readline
# from collections import deque

# def dfs(v):
#     visited_dfs[v] = 1
#     print(v, end= ' ')
#     for i in range(1,N+1):
#         if visited_dfs[i] == 0 and graph[v][i] == 1:
#             dfs(i)

# def bfs(v):
#     q = deque()
#     q.append(v)
#     visited_bfs[v] = 1
#     while q:
#         a = q.popleft()
#         print(a, end= ' ')
#         for i in range(1,N+1):
#             if visited_bfs[i] == 0 and graph[a][i] == 1:
#                 q.append(i)
#                 visited_bfs[i] = 1
    

# N ,M, V =map(int,input().split())

# graph = [[0] * (N+1)  for _ in range(N+1) ]
# visited_dfs = [0] * (N+1)
# visited_bfs = [0] * (N+1)
# for _ in range(M):
#    a, b = map(int,input().split())
#    graph[a][b] = graph[b][a] = 1
   
# dfs(V)
# print()
# bfs(V)


# ## 1012
# import sys
# input = sys.stdin.readline
# from collections import deque
# T = int(input())
# dx = [0,-1,1,0]
# dy = [-1,0,0,1]
# def bfs(x,y):
#     graph[x][y]=0
#     queue = deque()
    
#     queue.append((x,y))
    
#     while queue:
#         a_,b_ = queue.popleft()
#         for i in range(4):
#             a = a_ +  dx[i]
#             b = b_ + dy[i]
#             if 0<= a <N and 0<= b <M and graph[a][b] == 1:
#                 queue.append((a,b))
#                 graph[a][b] = 0
        
# for  _ in range(T):
#     M, N, K =map(int,input().split())
    
#     graph = [[0]*(M) for _ in range(N)]
#     for _ in range(K):
#         q, w = map(int,input().split())
#         graph[w][q] = 1
#     # print(graph)
#     cnt = 0
    
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 1:
#                 # print(i,j)
#                 bfs(i,j)
#                 graph[i][j] = 0
#                 cnt += 1
#                 # print(graph)
#     print(cnt)


## 9466 dfs
# import sys
# sys.setrecursionlimit(int(1e6))
# input = sys.stdin.readline

# def dfs(v):
#     global cnt
#     visited[v] = 1
#     team.append(v)
#     nxt =  graph[v]
#     if visited[nxt] == 0:
#         dfs(nxt)
#     else:
#         if nxt in team:
#             cnt += len(team) - team.index(nxt)
        
    
# for _ in range(int(input())):
#     N = int(input())
#     graph = [0] + list(map(int, input().split()))
#     visited = [0] *(N+1)
#     result = []
#     cnt = 0
    
#     for i in range(1,N+1):
#         if visited[i] == 0:
#             team = []
#             dfs(i)
    
#     print(N-cnt)
    

## 11404 Floyd

## 11780 Floyd

## 1753 Dijkstra
# import sys
# input = sys.stdin.readline 
# from heapq import *

# V, E = map(int, input().split())
# start = int(input())
# adj = [[] for _ in range(V+1)]

# for _ in range(E):
#     a,b,c = map(int,input().split())
#     adj[a].append((b,c))

# INF = int(1e9+7)
# dist = [INF] * (V+1)


# def dijkstra(s):
#     dist[s] = 0
#     heap = []
#     heappush(heap,(0, s))
    
#     while heap:
#         w , v = heappop(heap)
        
#         if dist[v] < w: continue
        
#         for nxt_v, nxt_w in adj[v]:
#             cost =  w + nxt_w
#             if  cost < dist[nxt_v]:
#                 dist[nxt_v] = cost
#                 heappush(heap,(cost,nxt_v))

# dijkstra(start)
# for i in range(1,V+1):
#     if dist[i] == INF:
#         print("INF")
#     else:
#         print(dist[i])


# import sys
# from heapq import *

# V, E = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(V+1)]

# for _ in range(E):
#     a, b, c = map(int,input().split())
#     graph[a].append((b,c))
    
# INF = int(1e9+7)
# dist = [INF] * (V+1)
# def dijkstra(s):
#     dist[s] = 0 
#     heap = []
#     heappush(heap, (0, s))
    
#     while heap:
#         w, v = heappop(heap)
        
#         if dist[v] < w: continue
        
#         for vv,ww in graph[v]:
#             if dist[vv] > ww+w:
#                 dist[vv] = ww +w
#                 heappush(heap,(dist[vv], ww))
                
# dijkstra(start)

# for i in range(1,V+1):
#     if dist[i] == INF: print("INF")
#     else: print(dist[i])

## 11779 

## 11657 Bellman

## 1865

## 1967 radius of tree

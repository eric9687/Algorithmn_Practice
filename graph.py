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

result_d = []
result_b = []

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
# import sys
# input  = sys.stdin.readline

# n = int(input())
# m = int(input())

# INF = int(1e9+7)
# graph = [[INF] * (n+1) for _ in range(n+1)]

# for _ in range(m):
#     a,b,c = map(int,input().split())
#     if graph[a][b] > c:
#         graph[a][b] = c

# for k in range(n+1):
#     for i in range(n+1):
#         for j in range(n+1):
#             if i != j:
#                 if graph[i][k] + graph[k][j] < graph[i][j]:
#                     graph[i][j] = graph[i][k] + graph[k][j]
                
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if graph[i][j] != INF:
#             print(graph[i][j],end=' ')
#         else: print("0", end=' ')
#     print()



## 11780 Floyd

# import sys
# input = sys.stdin.readline

# def find_route(a,b):
#     if route[a][b] == 0:
#         return []
#     else:
#         c = route[a][b]
#         return find_route(a,c) + [c] + find_route(c,b)
    
# n = int(input())
# m = int(input())

# INF = int(1e9+7)
# graph = [[INF]*(n+1) for _ in range(n+1)]
# route = [[0]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     a, b, c = map(int,input().split())
#     if graph[a][b] > c:
#         graph[a][b] = c
        
# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1, n+1):
#             if i != j:
#                 if graph[i][k] + graph[k][j] < graph[i][j]:
#                     graph[i][j] = graph[i][k] + graph[k][j]
#                     route[i][j] = k

# for i in range(1,n+1):
#     for  j in range(1,n+1):
#         if graph[i][j] != INF :  print(graph[i][j], end= ' ')
#         else: print(0, end= ' ')
#     print()
    

# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i == j or graph[i][j]==INF:
#             print(0)
#         else:
#             trace = [i] + find_route(i,j) + [j]
#             print(len(trace),*trace)
            
    




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
import sys
from heapq import *
input = sys.stdin.readline

def dijkstra(s):
    heap = []
    dist[s] = 0
    heappush(heap, (0,s))
    
    while heap:
        w, v = heappop(heap)
        
        if dist[v] != w: continue
        for vv, ww in graph[v]:
            if dist[vv] > w +ww:
                dist[vv] = w+ww
                heappush(heap,(dist[vv],vv))
                route[v] = vv

n = int(input())
m = int(input())

INF = int(1e9+7)
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
route = [[0] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())
dijkstra(start)

print(dist[end])
print


# ## 11657 Floyd
# import sys
# from typing import get_args
# input = sys.stdin.readline

# N, M = map(int,input().split())

# INF = int(1e9+7)
# graph= [[INF]*(N+1) for _ in range(N+1)]
# for _ in range(M):
#     a, b, c = map(int,input().split())
#     if graph[a][b] > c:
#         graph[a][b] = c
# is_possible = True
# for repeat in range(1,N+1):
#     for k in range(1, N+1):
#         for i in range(1, N+1):
#             for j in range(1,N+1):
#                 if i != j:
#                     if graph[i][k] + graph[k][j] < graph[i][j]:
#                         graph[i][j] = graph[i][k] + graph[k][j]
#                         if repeat == N:
#                             is_possible = False
# if is_possible == False:
#     print(-1)
# else:
#     for i in graph[1][2:]:
#         print(i if i != INF else -1)



## 11657 Bellman

# import sys
# input  = sys.stdin.readline
# INF = sys.maxsize

# n,m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# dp = [INF] * (n+1)
# is_possible = True

# for _ in range(m):
#     a,b,c = map(int, input().split())
#     graph[a].append((b,c))

# def BellmanFord(s):
#     global is_possible
#     dp[s] = 0
    
#     for repeat in range(1,n+1):
#         for i in range(1,n+1):
#             for n_n , wei in graph[i]:
#                 if dp[i] != INF and dp[n_n] > dp[i] + wei:
#                     dp[n_n] = dp[i] + wei
#                     if repeat == n:
#                         is_possible = False
#                         return
# BellmanFord(1)
# if not is_possible:
#     print(-1)
# else:
#     for i in dp[2:]:
#         print(i if i != INF else -1)
        



## 1865

# import sys
# input = sys.stdin.readline
# INF = sys.maxsize

# for _ in range(int(input())):
#     N, M, W = map(int, input().split())
#     graph = [[] for _ in range(N+1)]
    
#     for _ in range(M):
#         a,b,c = map(int,input().split())
#         graph[a].append((b,c))
#         graph[b].append((a,c))
#     for _ in range(W):
#         a, b, c = map(int, input().split())
#         graph[a].append((b,-c))
    
#     dist = [INF]*(N+1)
#     is_Possible =True
#     def BellmanFord():
#         global is_Possible
        
#         for repeat in range(1,N+1):
#             for i in range(1,N+1):
#                 for v,c in graph[i]:
#                     if  dist[v] >  dist[i] + c:
#                         dist[v] = dist[i] + c
#                         if repeat == N:
#                             is_Possible = False
                        
                            
    
#     BellmanFord()

#     print("NO" if is_Possible else "YES")
    
    

## 1967 radius of tree

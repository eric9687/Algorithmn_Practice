# #1719 - floyd warshall
# import sys
# input = sys.stdin.readline
# n,m =  map(int,input().split())
# inf = 10**9
# bus = [[inf]*(n+1) for _ in range(n+1) ] 
# check = [['-']*(n+1) for _ in range(n+1)]

# for _ in range(m):
#     i,j,k = map(int,input().split())
#     if k < bus[i][j]:
#         bus[i][j] = k
#         bus[j][i] = k
#         check[i][j] = str(j)
#         check[j][i] = str(i)

# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i != j :
#                 if (bus[i][k]+bus[k][j] < bus[i][j]) :
#                     bus[i][j] = bus[i][k] + bus[k][j]
#                     check[i][j] = check[i][k]
#                 # if bus[i][j] == 0 and  bus[i][k] != 0 and bus[k][j] != 0:
#                 #     bus[i][j] = bus[i][k] + bus[k][j]

# for i in range(1,n+1):
#     for j in range(1,n+1):
        
#         print(check[i][j],end= ' ')
        
#     print()


# #1719 - dijkstra
# import sys
# import math
# import heapq
# inf =  10**9
# input = sys.stdin.readline
# n,m =  map(int,input().split())
# graph = [[] for _ in range(n+2)]

# for _ in range(m):
#     i,j,k = map(int, input().split())
#     graph[i].append((j,k))
#     graph[j].append((i,k))

# total_dis = []
# total_path = []

# for i in range(1,n +1):
#     dist = [inf for _ in range(n+2)]
#     path = [-1 for _ in range(n+2)]
#     edges = []

#     dist[i] = 0
#     heapq.heappush(edges, (dist[i],i))

#     while edges:
#         print("--------------")
#         print(edges)
#         cost, pos = heapq.heappop(edges)
#         if dist[pos] < cost:
#             continue
#         for p,c in graph[pos]:
#             c += cost
#             if dist[p] >c:
#                 dist[p] = c
#                 heapq.heappush(edges,(c,p))
#                 path[p] = pos
#             print(edges)
#     total_dis.append(dist)
#     total_path.append(path)

# print(total_path)





# #11404
# import sys
# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# inf = 10**9
# bus = [[inf]*(n+1) for _ in range(n+1) ] 

# for _ in range(m):
#     i,j,k = map(int,input().split())
#     if k < bus[i][j]:
#         bus[i][j] = k

# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i != j :
#                 if (bus[i][k]+bus[k][j] < bus[i][j]) :
#                     bus[i][j] = bus[i][k] + bus[k][j]
#                 # if bus[i][j] == 0 and  bus[i][k] != 0 and bus[k][j] != 0:
#                 #     bus[i][j] = bus[i][k] + bus[k][j]

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if bus[i][j] != inf:
#             print(bus[i][j],end= ' ')
#         else:
#             print(0,end= ' ')
#     print()



# #1240 Floyd 시간 초과 => dijkstra
# import sys
# from heapq import heappush, heappop
# input = sys.stdin.readline
# N, M = map(int, input().split())
# inf = 10**9
# graph =  [[] for _ in range(N+1)]
# dis = [[inf]*(N+1) for _ in range(N+1)]
# visit = [[0]*(N+1) for _ in range(N+1)]

# def dijkstra(i):
#     dis[i][i] = 0
#     h = [[0,i]]

#     while h:
#         k, j = heappop(h)
#         if visit[i][j] or k > dis[i][j]:
#             continue
#         visit[i][j] = 1
#         for w, v in graph[j]:
#             if dis[i][v] > w + dis[i][j] and not visit[i][v]:
#                 dis[i][v] = w + dis[i][j] 
#                 heappush(h, [dis[i][v], v])



# for _ in range(N-1):
#     u, v, w = map(int, input().split())
#     graph[u].append([w, v])
#     graph[v].append([w, u])

# for _ in range(M):
#     i, j = map(int, input().split())
#     dijkstra(i)
#     print(dis[i][j])


# #14940
# import sys
# from collections import deque
# input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# visit =  [[0]*m for _ in range(n)]

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# q = deque()

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 2:
#             q.append((i,j))
# #BFS
# while q:
#     x, y = q.popleft()
#     for i in range(4):
#         n_x, n_y = x + dx[i], y +dy[i]
#         if 0 <= n_x < n and 0 <= n_y <m and graph[n_x][n_y] == 1 and visit[n_x][n_y] == 0:
#             visit[n_x][n_y] = visit[x][y] + 1
#             q.append((n_x, n_y))

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1 and visit[i][j] == 0 :
#             visit[i][j] = -1

# for i in range(n):
#     for j in range(m):
#         print(visit[i][j],end = ' ')
#     print()

# #1504
# import sys
# import heapq
# input =  sys.stdin.readline
# inf = 10**9

# N, E = map(int, input().split())
# graph  = [[] for _ in range(N+1)]

# for _ in range(E):
#     u, v, w = map(int, input().split())
#     graph[u].append((w,v))
#     graph[v].append((w,u))

# dis =[[]*(N+1) for _ in range(N+1)]

# def dijkstra(i):
#     for _ in range(N+1):
#         dis[i].append(inf)
#     dis[i][i] = 0
#     heap = [[dis[i][i],i]]

#     while heap:
#         k, u = heapq.heappop(heap)
#         if k > dis[i][u]:
#             continue
#         for w,v in graph[u]:
#             if dis[i][v] > dis[i][u] + w:
#                 dis[i][v] = dis[i][u] + w
#                 heapq.heappush(heap, [dis[i][v],v])
    

# u, v = map(int, input().split())
# for i in [1,u,v]:
#     dijkstra(i)


# if u == v or u ==N or v == 1:
#     print(-1)
# else:
#     distance = dis[1][u] + dis[u][v] + dis[v][N]
#     com_distance = dis[1][v] + dis[v][u] + dis[u][N]
#     if com_distance < distance:
#         distance = com_distance
#     if distance >= inf:
#         print(-1)
#     else:
#         print(distance)


# 1753
import sys
import heapq
input =  sys.stdin.readline
inf = 10**9

N, E = map(int, input().split())
K = int(input())
graph  = [[] for _ in range(N+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))
  

dis =[[]*(N+1) for _ in range(N+1)]

def dijkstra(i):
    for _ in range(N+1):
        dis[i].append(inf)
    dis[i][i]= 0
    heap = [[0,i]]

    while heap:
        k, u = heapq.heappop(heap)
        if dis[i][u] < k:
            continue
        for w,v in graph[u]:
            if dis[i][v] > k + w:
                dis[i][v] = k + w
                heapq.heappush(heap, [dis[i][v],v])

dijkstra(K)

for i in range(1,len(dis[K])):
    print(dis[K][i] if dis[K][i] != inf else "INF")


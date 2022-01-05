## 2667
# import sys
# input = sys.stdin.readline

# N = int(input())
# graph = []

# for _ in range(N):
    
#     graph.append(list(input().rstrip()))

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# def dfs(x,y):
#     global cnt
#     if 0 <= x < N and 0 <= y < N and graph[x][y] == '1':
#         cnt += 1
#         graph[x][y] = '0'
#         for i in range(4):
#             dfs(x+dx[i],y+dy[i])
        
# result = []

# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == '1':
#             cnt = 0 
#             dfs(i,j)
#             result.append(cnt)
# print(len(result))
# result = sorted(result)
# for r in result: print(r)

## 2583
# import sys
# input = sys.stdin.readline

# M, N , K = map(int,input().split())
# graph = []
# for _ in range(N):
#     graph.append([0]*M)
# for _ in range(K):
#     x1, y1, x2, y2 = map(int,input().split())
#     for x in range(x1,x2):
#         for y in range(y1,y2):
#             graph[x][y] = 1


# def dfs(x,y):
#     global cnt 
#     graph[x][y] = 1
#     cnt += 1
#     dx = [0, 0 , 1, -1]
#     dy = [1, -1, 0, 0]
#     for i in range(4):
#         if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M:
#             if graph[x+dx[i]][y+dy[i]] == 0:
#                 dfs(x+dx[i],y+dy[i])

# result = []
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 0:
            
#             cnt = 0
#             dfs(i,j)
#             result.append(cnt)
# print(len(result))
# print(*sorted(result))

# ## 2468

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e9+7))
# N = int(input())
# graph = []
# height = []

# for _ in range(N):
#     a = list(map(int,input().split()))
#     graph.append(a)
#     height += a
# heights = max(height)


# def dfs(x,y,k):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     visited[x][y] = 1
#     for p in range(4):
#         nxt_x = x + dx[p]
#         nxt_y = y + dy[p]
#         if 0 <= nxt_x< N and 0 <= nxt_y < N and visited[nxt_x][nxt_y] == 0 and graph[nxt_x][nxt_y] > k:
#             dfs(nxt_x,nxt_y,k)
# max_cnt = 0 
# for h in range(heights):
#     cnt = 0
#     visited = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == 0 and graph[i][j] > h:
#                 dfs(i,j,h)
#                 cnt += 1
                
#     max_cnt = max(max_cnt,cnt)
    
# print(max_cnt)


## 16929
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e9))

# m,n = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(m)]

# cycle = False
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def dfs(x,y,alpha,cnt,sx,sy):
#     global cycle
#     if cycle == True:
#         return
#     for  i in range(4):
#         nxt_x = x + dx[i]
#         nxt_y = y + dy[i]
#         if cnt >= 4 and nxt_x == sx and nxt_y == sy:
#             cycle = True
#         if 0<= nxt_x < m and 0 <= nxt_y < n and visited[nxt_x][nxt_y] == 0 and graph[nxt_x][nxt_y] == alpha:
#             visited[nxt_x][nxt_y] = 1
#             dfs(nxt_x,nxt_y,alpha,cnt+1,sx,sy)

# for i in range(m):
#     for j in range(n):
#         visited = [[0]*n for _ in range(m)]
#         visited[i][j] = 1
#         dfs(i,j,graph[i][j],1,i,j)
#         if cycle : break
#     if cycle : break

    
# print("Yes" if cycle else "No")

## 16964

# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [set() for _ in range(n+1)]

# for _ in range(n-1):
#     a,b = map(int,input().split())
#     graph[a].add(b)
#     graph[b].add(a)
    
# answer = list(map(int,input().split()))

# stack  = [answer[0]]
# flag = True
# def sol():
#     if answer[0] != 1:
#         return False
#     for a in answer:
#         if a==1:
#             continue
#         while stack and a not in graph[stack[-1]]:
#             stack.pop()
#         if not stack  :
#             return False
#         stack.append(a)
#     return True
    
# if sol(): print(1)
# else: print(0)

            
## 1743
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

n,m,k = map(int,input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    graph[a][b] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    global cnt
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= n and 1 <= ny <=m and graph[nx][ny] == 1:
            cnt += 1
            dfs(nx,ny)

max_size = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j] == 1:
            cnt = 1
            dfs(i,j)
            max_size = max(max_size,cnt)
            
print(max_size)



    


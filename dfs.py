import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# N = int(input())
# graph = [[] for i in range(N+1)]
# for _ in range(N-1):
#     a, b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# parent = [0] * (N+1)

# def dfs(start):
#     for i in graph[start]:
#         if parent[i] == 0 :
#             parent[i] = start
#             dfs(i)

# dfs(1)
# # print(parent)
# for i in range(2,len(parent)-1):
#     print(parent[i])
###########################
# N = int(input())
# tree = {}
# for _ in range(N) :
#     root, left, right = map(str,input().split())
#     tree[root]= [left,right]

# pre_=[]
# ino_=[]
# post_ = []


# def pre(i):
#     if i != ".":
#         pre_.append(i)
#         pre(tree[i][0])
#         pre(tree[i][1])

# def ino(i):
#     if i != ".":
        
#         ino(tree[i][0])
#         ino_.append(i)
#         ino(tree[i][1])

# def post(i):
#     if i != ".":
        
#         post(tree[i][0])
#         post(tree[i][1])
#         post_.append(i)

# pre('A')
# ino('A')
# post('A')
# print("".join(pre_))
# print("".join(ino_))
# print("".join(post_))
##########################
# N, M = map(int, input().split())
# count = 0
# graph = [[] for _ in range(N+1)]
# visited = [0]*(N+1)
# for _ in range(M):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a) 

# def dfs(i):
#     visited[i] = 1
#     for j in graph[i]:
#         if visited[j] == 0:
#             dfs(j)

# for i in range(1,N+1):
#     if visited[i] == 0:
#         dfs(i)
#         count+=1

# print(count)
######################
# for _ in range(int(input())):
#     n = int(input())
#     choice = [0] + list(map(int,input().split()))


#     def dfs(i):
#         global count
#         global main_stu
#         if i != 0:
#             route.append(i)
#             if len(route) > 1 and route[-1] == main_stu :
#                 count += len(route)-1
#                 for k in route:
#                     choice[k] =0
#                 route.clear()
                
#             else:
#                 dfs(choice[i])
#         else:
#             route.clear()
        
#     for i in range(1,n+1):
#         if choice[i] == i:
#             count += 1
#             choice[i] = 0
    
#     count =0
#     route = []
#     for i in range(1,n+1):
#         main_stu = i
#         if choice[i] != 0:
#             dfs(i)
        
        

#     print(n-count)
#################################################
# import sys
from copy import deepcopy

# 오타에 조심해야 한다. i, j 위치를 바꿔서 쓴다거나, deepcopy 를 잘못하면 바로 틀렸다고 나온다.
# p: 행이나 열에서 블록이 이동하게 될 가장 끝의 위치
# x: 블록이 합쳐지는것을 표현하기 위한 변수

def move_right(board):
    for i in range(N):
        
        exist = []
        for j in board[i]:
            if j != 0:
                exist.append(j)
        
        k=0
        for j in range(N):
            
            if j < N -len(exist) :
                board[i][j] = 0
            else:
                board[i][j] = exist[k]
                k += 1
    
    for i in range(N):
        for j in range(N-1,0,-1):
            if board[i][j] == board[i][j-1]:
                board[i][j] *= 2
                board[i][j-1] =0
    
    for i in range(N):
        
        exist = []
        for j in board[i]:
            if j != 0:
                exist.append(j)
        
        k=0
        for j in range(N):
            
            if j < N -len(exist) :
                board[i][j] = 0
            else:
                board[i][j] = exist[k]
                k += 1
    return board

def move_left(board):
    for i in range(N):
        
        exist = []
        for j in board[i]:
            if j != 0:
                exist.append(j)
        
        k=0
        for j in range(N):
            if k < len(exist):
                board[i][j] = exist[k]
                k += 1
            else:
                board[i][j] = 0

    for i in range(N):
        for j in range(0,N-1,1):
            if board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                board[i][j+1] =0
    
    for i in range(N):
        
        exist = []
        for j in board[i]:
            if j != 0:
                exist.append(j)
        
        k=0
        for j in range(N):
            if k < len(exist):
                board[i][j] = exist[k]
                k += 1
            else:
                board[i][j] = 0
    return board

def move_up(board):
    for j in range(N):
        exist= []
        for i in range(N):
            if board[i][j] != 0:
                exist.append(board[i][j])
        k=0
        for i in range(N):
            if k < len(exist):
                board[i][j] = exist[k]
                k += 1
            else:
                board[i][j] = 0
    
    for i in range(0,N-1,1):
        for j in range(N):
            if board[i][j] == board[i+1][j]:
                board[i][j] *= 2
                board[i+1][j] =0
    
    for j in range(N):
        exist= []
        for i in range(N):
            if board[i][j] != 0:
                exist.append(board[i][j])
        k=0
        for i in range(N):
            if k < len(exist):
                board[i][j] = exist[k]
                k += 1
            else:
                board[i][j] = 0
    return board

def move_down(board):
    for j in range(N):
        exist= []
        for i in range(N):
            if board[i][j] != 0:
                exist.append(board[i][j])
        k=0
        for i in range(N):
            if i < N-len(exist):
                board[i][j] = 0
            else:
                board[i][j] = exist[k]
                k += 1
    
    for i in range(N-1,0,-1):
        for j in range(N):
            if board[i][j] == board[i-1][j]:
                board[i][j] *= 2
                board[i-1][j] =0
    
    for j in range(N):
        exist= []
        for i in range(N):
            if board[i][j] != 0:
                exist.append(board[i][j])
        k=0
        for i in range(N):
            if i < N-len(exist):
                board[i][j] = 0
            else:
                
                board[i][j] = exist[k]
                k += 1
    return board

def dfs(board , count, result):
    global max_result
    if count ==5:
        max_result = max(max_result,max(map(max,board)))
        return
    
    dfs(move_left(deepcopy(board)), count + 1) # 블록을 좌측으로 이동
    dfs(move_right(deepcopy(board)), count + 1) # 블록을 우측으로 이동
    dfs(move_up(deepcopy(board)), count + 1) # 블록을 상단으로 이동
    dfs(move_down(deepcopy(board)), count + 1)

    

max_result =0
N=4
board =[[2,0,0,2],[2,4,0,0],[2,0,0,0],[0,4,0,4]]
move_down(board)
dfs(board,0)
print(max)






    

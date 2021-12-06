#1717
# import sys
# sys.setrecursionlimit(10**6)   ## 재귀문제에서 추가해주자!
# input = sys.stdin.readline

# n, m = map(int,input().split())
# par = [i for i in range(n+1)]

# def Find(x):
#     if x == par[x]: return x
#     par[x] = Find(par[x])
#     return par[x]

# def Union(a,b):
#     a = Find(a)
#     b = Find(b)
#     if a == b:
#         return
#     if a < b:
#         par[b] = a
#     else:
#         par[a] = b
        
# for _  in range(m):
#     i, a, b = map(int,input().split())
#     if i == 0:
#         Union(a,b)
#     else:
#         if Find(a) == Find(b):
#             print("YES")
#         else:
#             print("NO")
            
            
## 11724
# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())
# point = [i for i in range(n+1)]

# def Find(x):
#     if x == point[x]: return point[x]
#     point[x] = Find(point[x])
#     return point[x]

# def Union(a,b):
#     a = Find(a)
#     b = Find(b)
#     if a==b: return
#     if a < b:
#         point[b] = a
#     else: 
#         point[a] = b

# for _ in range(m):
#     a,b = map(int, input().split())
#     Union(a,b)

# cnt = 0
# root = []
# for i in range(1, n+1):
#     if Find(i) not in root:
#         root.append(Find(i))
# print(len(root))

## 1976
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# N = int(input())
# M = int(input())
# load = [i for i in range(N+1)]

# def Find(x):
#     if x ==  load[x]: return load[x]
#     load[x] = Find(load[x])
#     return load[x]

# def Union(a,b):
#     a = Find(a)
#     b = Find(b)
#     if a==b: return
#     if a < b:
#         load[b] = a
#     else: load[a] =b

# for i in range(1,N+1):
#     a = [0]+list(map(int, input().split()))
#     for j in range(1,N+1):
#         if a[j] == 1:
#             Union(i,j)
            
    
# travel  = list(map(int, input().split()))
# cnt = 0
# for i in range(M-1):
#     if Find(travel[i]) == Find( travel[i+1]):
#         cnt +=1
#     else:
#         break

# if cnt == M-1:
#     print("YES")
# else: print("NO")

# 16562
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# N, M, K = map(int,input().split())
# fee = list(map(int,input().split()))
# friend = [0]
# for i in range(N):
#     friend.append([i+1, fee[i]])

# def Find(x):
#     if x ==  friend[x][0]: return friend[x][0]
#     friend[x][0] = Find(friend[x][0])
#     return friend[x][0]

# def Union(a,b):
#     a = Find(a)
#     b = Find(b)
    
#     if a==b: return
#     if a < b:
#         friend[b][0] = a
#     else: friend[a][0] =b
        
#     if friend[a][1] > friend[b][1]:
#         friend[a][1] = friend[b][1]
#     else:
#         friend[b][1] = friend[a][1]

# for _ in range(M):
#     a,b = map(int,input().split())
#     Union(a,b)

# inssa = []
# for i in range(1,N+1):
#     if Find(i) not in inssa:
#         inssa.append(Find(i))
# money = 0
# for i in inssa:
#     money += friend[i][1]
# if money <= K:
#     print(money)
# else: print("Oh no")


## 16724
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# N, M = map(int,input().split())
# direction = []
# G = [i for i in range(N*M)]

# def Find(x):
#     if x == G[x]: return x
#     G[x] = Find(G[x])
#     return G[x]

# def Union(a,b):
#     a = Find(a)
#     b = Find(b)
#     if a == b: return
#     G[b] = a
    
# for _ in range(N):
#     st = input().rstrip()
#     for ch in st:
#         direction.append(ch)

    
# for i in range(N):
#     for j in range(M):
        
#         if direction[i*M + j] == 'D':
#             Union(i*M + j, M*(i+1) + j)
#         elif direction[i*M + j] == 'U':
#             Union(i*M + j, M*(i-1) + j)
#         elif direction[i*M + j] == 'L':
#             Union(i*M + j , M*i + j -1)
#         else: Union(i*M + j , M*i + j +1)
    
# cnt = 0
# for i in range(N*M):
#     if G[i] == i: cnt += 1
# print(cnt)
    
    
## 10775
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

G = int(input())
P = int(input())
flight = []
for _ in range(P):
    flight.append(int(input()))
parent = [i for i in range(G+1)]

def Find(x):
    if x == parent[x]: return x
    parent[x] = Find(parent[x])
    return parent[x]

def Union(a,b):
    a = Find(a)
    b = Find(b)
    parent[a] = b
    
cnt = 0
for i in flight:
    if Find(i) == 0:
        break
    Union(Find(i), Find(i)-1)
    cnt += 1
print(cnt)

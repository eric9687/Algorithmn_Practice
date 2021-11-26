#1717
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# Union-Find
par = [0] * (n+1) 
for i in range(n+1):
    par[i] = i

def Find(x): # x의 루트노드를 찾음
    if x == par[x]: return x
    par[x] = Find(par[x])
    return par[x]

def Union(a, b): # a와 b의 집합을 합침
    a = Find(a)
    b = Find(b)
    if a==b:
        return
    if a < b:
        par[b] = a
    else:
        par[a] = b


# 간선 입력
for _ in range(m):
    i,a, b = map(int, input().split())
    if i == 0:
        Union(a, b)
    else:
        if Find(a) == Find(b):
            print("Yes")
        else:
            print("No")
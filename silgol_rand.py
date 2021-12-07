#13422
# import sys
# from collections import deque

# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     N, M, K = map(int, input().split())
#     cnt = 0
#     money = list(map(int, input().split()))
#     if N == M:
#         if sum(money)<K:
#             print(1)
#         else:
#             print(0)
#     else:
#         money = money + money[:M-1]
#         steal = sum(money[:M])
#         before = 0
#         if steal < K:
#             cnt += 1
#         for i in range(M,N+M-1):
#             steal = steal - money[before] + money[i]
#             if steal < K:
#                 cnt+= 1
#             before += 1
#         print(cnt)
    


    


#     print(count)


    
## 4307
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    stick, n = map(int,input().split())
    
    min_ant = []
    max_ant = []
    for _ in range(n):
        ant = int(input())
        if 2*ant > stick:
            min_time = stick - ant
            max_time = ant
        else:
            min_time = ant
            max_time = stick - ant
        min_ant.append(min_time)
        max_ant.append(max_time)
    print(max(min_ant), max(max_ant))
        
        
        
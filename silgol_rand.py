#13422
# import sys
# from collections import deque

# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     N, M, K = map(int, input().split())
#     count = 0
#     money = list(map(int, input().split()))
#     total =sum(money)


    # if total < K: count +=1

    # if N != M:
    #     for i in range(N):
    #         total -= money[i]
    #         next_house = i + M
    #         if next_house >= N:
    #             next_house -= N
    #         if total < K: count +=1


    # print(count)


    
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
        
        
        
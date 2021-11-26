#13422
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    count = 0
    money = list(map(int, input().split()))
    total =sum(money)


    if total < K: count +=1

    if N != M:
        for i in range(N):
            total -= money[i]
            next_house = i + M
            if next_house >= N:
                next_house -= N
            if total < K: count +=1


    print(count)


    

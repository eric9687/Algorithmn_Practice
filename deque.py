## 5430
# import sys
# input = sys.stdin.readline
# from collections import deque

# for _ in range(int(input())):
#     order = input().rstrip()
#     n=int(input())
#     numss = input().rstrip()
#     nums = numss[1:-1].split(',')
#     nums = deque(nums)
    
        
#     flag = 0
#     err = True
#     if n == 0 and order:
#         nums = []
        
#     for o in order:
#         if o == "R":
#             if flag == 0:
#                 flag = 1
#             else:
#                 flag = 0
#         else:
#             if nums:
#                 if flag ==1:
#                     nums.pop()
#                 else:
#                     nums.popleft()
#             else:
#                 err = False
#                 break
#     if err:
#         if flag == 0:
#             print("["+",".join(nums)+"]")
#         else:
#             nums.reverse()
#             print("["+",".join(nums)+"]")
#     else: print("error")
    
    
## 3190

# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# k = int(input())
# apple = [list(map(int,input().split())) for i in range(k)]
# tl = int(input())
# ti, turn = 0, [list(input().split()) for i in range(tl)]

# for i in turn:
#     i[0] = int(i[0])

# snake,t,direction = deque(),0,0
# snake.append([1,1])

# head = [1,1]

# while(True):
#     t+=1
    
#     # 이동
#     if direction == 0:
#         head[1] += 1
#     elif direction == 1:
#         head[0] += 1
#     elif direction == 2:
#         head[1] -= 1
#     else:
#         head[0] -= 1
    
    
#     # 부딪힘
#     if head in snake:
#         print(t)
#         break
#     if head[0] > n or head[0] < 1 or head[1] > n or head[1] < 1:
#         print(t)
#         break
        
#     # 사과
#     if head not in apple:
#         snake.popleft()
#     else:
#         apple.remove(head)
    
#     # 머리 위치 저장
#     snake.append([head[0],head[1]])
    
#     # 방향 전환
#     if ti < tl and t == turn[ti][0]:
#         if turn[ti][1] == "D":
#             direction = (direction + 1)%4
#         else:
#             direction = (direction - 1)%4
#         ti += 1
        
        
## 19591

import sys
input = sys.stdin.readline

def yunsuan(a,y,b):
    if y == "+":
        return a + b
    elif y == "-":
        return a - b
    elif y == "*":
        return a*b
    else:
        ans = abs(a) // abs(b)
        if a*b >0:
            return ans
        else:
            return -ans
        
NS = list(input().rstrip())
if NS[0] == "-":
    NS[1] = "-"+NS[1]
    NS = NS[1:]

stack=[]
S=[]
for nn in NS:
    if stack and nn in "+-*/":
        S.append(int(''.join(stack)))
        S.append(nn)
        stack = []
    else:
        stack.append(nn)
if stack:
    S.append(int(''.join(stack)))

# print(S)
pr = {"+":0, "-":0, "*": 1, "/":1}

while True:
    one = S[:3]
    two = S[-3:]
    
    if len(S) <= 3:
        break
    if pr[one[1]] == pr[two[1]]:
        result1 = yunsuan(one[0],one[1],one[2])
        result2 = yunsuan(two[0],two[1],two[2])
        if result1 >= result2:
            S[0]=result1
            S = [S[0]]+S[3:] 
        else:
            S[-1]= result2
            S = S[:-3] +  [S[-1]]
    elif pr[one[1]] > pr[two[1]]:
        S[0] =  yunsuan(one[0],one[1],one[2])
        S = [S[0]]+ S[3:] 
    else:
        S[-1] =    yunsuan(two[0],two[1],two[2])
        S= S[:-3]+[S[-1]]
    # print(S)
if len(S) == 3:
    print(yunsuan(S[0],S[1],S[2]))
else:
    print(S[0])
    

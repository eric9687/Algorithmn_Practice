## 22866
# import sys
# from typing import AbstractSet

# input = sys.stdin.readline

# S = input().rstrip()

# stack  = []
# l = 0
# for ch in S:
#     if ch.isdigit():
#         l += 1
#         tmp  = ch
#     elif ch == '(':
#         stack.append((tmp, l-1))
#         l = 0
#     else:
#         multi, preL = stack.pop()
#         l = l * int(multi) + preL

# print(l)
# # 3(2) => 222,  4(5) => 5555


# # 33(562(71(9)))
# # 33(562(79))
# # 33(567979)
# # 3567979567979567979

# # stack = [(곱할 수, 더할 수)]


# ## 2841
# import sys
# input = sys.stdin.readline

# N, P = map(int, input().split())

# stack = [[] for _ in range(N+1)]

# finger = 0
# for _ in range(N):
#     l, pr = map(int, input().split())
#     if stack[l]:
#         while True:
#             before = stack[l][-1]
#             if before > pr:
#                 stack[l].pop()
#                 finger += 1
#             elif before == pr:
#                 stack[l].pop()
#                 finger -= 1
#                 break
#             else:
#                 break
#             if not stack[l]:
#                 break
#     finger += 1
#     stack[l].append(pr)
# print(finger)


## 2800
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# S = list(input().rstrip())

# stack = []
# couple = []
# answer = set()

# for i in range(len(S)):
    
#     if S[i] == '(':
#         stack.append(i)
#     elif S[i] == ')':
#         couple.append((stack.pop(), i))

# for i in range(1,len(couple)+1):
    
#     couple_comb = combinations(couple,i)
#     for j in couple_comb:
#         tmp = S[:]
#         for (l,r) in j:
#             tmp[l] = ''
#             tmp[r] = ''
#         answer.add(''.join(tmp))
# # print(set(answer))
# for i in sorted(list(answer)):
#     print(i)


## 22866

# import sys
# input = sys.stdin.readline

# N= int(input())
# B = [0] + list(map(int,input().split()))
# stack = [(1,B[1])]
# Arr = [0]*(N+1)
# for i in range(2,N+1):
#     while stack:
#         if stack[-1][1] < B[i]:
#             Arr[stack[-1][0]] = i
#             stack.pop()
#         else:
#             break
#     stack.append((i,B[i])) 
        
# print(Arr)



## 16120
# import sys
# input = sys.stdin.readline

# S = input()

# if S == 'P' or S == 'PPAP':
#     print('PPAP')
# else: 
#     stack = []
#     ppap = ['P','P','A','P']
#     for ch in S:
#         stack.append(ch)
#         if stack[-4:] == ppap:
#             for _ in range(3):
#                 stack.pop()
                
#     if stack == ['P'] or ppap:
#         print("PPAP")
#     else:
#         print('NP') 

## 6549
import sys
input = sys.stdin.readline

while True:
    N, *H = list(map(int, input().split()))+[0]
    if N ==0:
        break
    stack = []
    i = 0
    ans = 0
    while i < N+1:
        if not stack or H[stack[-1]] <= H[i]:
            stack.append(i)
            i += 1
        else:
            height = H[stack.pop()]
            if stack:
                ans = max(ans, height * (i - stack[-1]-1))
            else:
                ans = max(ans, height * i)
    print(ans)
    
        
            
    
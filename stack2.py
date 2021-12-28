## https://www.acmicpc.net/workbook/view/8432

## 10828
# import sys
# input = sys.stdin.readline
# stack = []
# for _ in range(int(input())):
#     a =input().split()
#     if a[0] == "push":
#         stack.append(int(a[1]))
#     elif a[0] == "pop":
#         if stack:
#             print(stack.pop())
#         else:
#             print("-1")
#     elif a[0] == "size":
#         print(len(stack))
#     elif a[0] == "empty":
#         if stack:
#             print("0")
#         else: print("1")
#     elif a[0] == "top":
#         if stack : print(stack[-1])
#         else: print("-1")
        
        
## 9012
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     stack = []
#     S = input()
#     for ch in S:
#         if ch == '(':
#             stack.append(ch)
#         elif ch == ')':
#             if stack and stack[-1] == '(': stack.pop()
#             else: stack.append(ch)
#     if len(stack) == 0:
#         print("YES")
#     else:
#         print("NO")

##4949

# import sys
# input = sys.stdin.readline

# while True:
#     stack = []
#     S = input().rstrip()
#     if S == ".":
#         break
#     for ch in S:
#         if ch == '(':
#             stack.append(ch)
#         elif ch == '[':
#             stack.append(ch)
#         elif ch == ')':
#             if stack and stack[-1] == '(': stack.pop()
#             else: stack.append(ch)
#         elif ch == ']':
#             if stack and stack[-1] == '[': stack.pop()
#             else: stack.append(ch)
#     if len(stack) == 0:
#         print("yes")
#     else:
#         print("no")

##10799
# import sys
# input = sys.stdin.readline
# j = int(input())
# i = 1
# stack = []
# answer = []
# for k in range(j):
#     n = int(input())
#     while i <= n :
#         answer.append("+")
#         stack.append(i)
#         i += 1
#     if stack[-1] == n:
#         answer.append("-")
#         stack.pop()
#     else:
#         print("NO")
#         break
#     if k == j-1:
#         for ans in answer:
#             print(ans)
#         break
    
## 1918
# import sys
# input = sys.stdin.readline

# S= input()
# answer = ""
# stack = []
# for ch in S:
#     if ch.isalpha():
#         answer +=ch
#     else:
#         if ch == "(":
#             stack.append(ch)
#         elif ch in "*/":
#             while stack and stack[-1] in "*/":
#                 answer += stack.pop()
#             stack.append(ch)
#         elif ch in "+-":
#             while stack and stack[-1] != "(":
#                 answer += stack.pop()
#             stack.append(ch)
#         elif ch == ")":
#             while stack and stack[-1] != "(":
#                 answer += stack.pop()
#             stack.pop()
# while stack:
#     answer += stack.pop()
# print(answer)


## 9935

import sys
input = sys.stdin.readline

S = input().rstrip()
ex = input().rstrip()

stack = []


for ch in S:
    stack.append(ch)
    if stack and "".join(stack[-(len(ex)):]) == ex:
        for _ in range(len(ex)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
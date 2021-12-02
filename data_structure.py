## 1620
# import sys
# input = sys.stdin.readline

# N, M =map(int,input().split())

# pkm_name = {}

# for i in range(1,N+1):
#     pkm = input().rstrip()
#     pkm_name[i] = pkm

# pkm_index = {v:k for k,v in pkm_name.items()}

# for _ in range(M):
#     question = input().strip()
#     if question.isdigit():
#         print(pkm_name[int(question)])
#     else:
#         print(pkm_index[question])


## 11279
# import heapq
# import sys
# input =  sys.stdin.readline

# heap = []
# for _ in range(int(input())):
#     x = int(input())
#     if x==0:
#         if heap:
#             print(heapq.heappop(heap)[1])
#         else: print("0")
#     else:
#         heapq.heappush(heap,(-x,x))

## 1863
# import sys
# input  = sys.stdin.readline
# B = []
# cnt = 0
# N = int(input())
# for _ in range(N):
#     x, y = map(int, input().split())
#     B.append(y)

# stack = []
# for i in range(N):
    
#     while stack and stack[-1] > B[i]:
#         stack.pop()
        
#     if B[i]: 
#         if(not stack or stack[-1] < B[i]):
#             stack.append(B[i])
#             cnt += 1

# print(cnt)


## 7662  이중 우선순위 큐: 다른 언어같은 경우는 여러가지 스택도 되고...하지만 파이썬은 유일한 방법
# import heapq
# def sync(arr):
#     while arr and id[arr[0][1]] == 0:
#         heapq.heappop(arr)

# T = int(input())
# for test_case in range(T):
#     max_arr = []
#     min_arr = []
#     id = [0] * 1000000
#     K = int(input())
#     count = 0
#     for i in range(K):
#         S, num = input().split()

#         if S == "I":
#             heapq.heappush(max_arr, (-1 * int(num), i))
#             heapq.heappush(min_arr, (int(num),i))
#             id[i] = 1
            
#         else:

#             if num == "1":
#                 sync(max_arr)
#                 if max_arr:
#                     id[max_arr[0][1]] = 0
#                     heapq.heappop(max_arr)

#             elif num == "-1":
#                 sync(min_arr)
#                 if min_arr:
#                     id[min_arr[0][1]] = 0
#                     heapq.heappop(min_arr)

#     sync(max_arr)
#     sync(min_arr)

#     if len(max_arr) == 0:
#         print("EMPTY")
#     else:
#         print(-1 * max_arr[0][0], end =" ")
#         print(min_arr[0][0])
        
        
## 22942
import sys
input = sys.stdin.readline

C = []
one = []
for i in range(int(input())):
    x,r = map(int, input().split())
    C.append((x-r, i, 'l'))
    C.append((x+r, i, 'r'))
    one.append(x-r)
    one.append(x+r)


if sorted(one) != sorted(list(set(one))):  ## set은 완전한 오름차순 정렬이 아니고,
                                           ## 선 양수, 후 음수
    print("NO")
else:

    C.sort(key= lambda x: x[0])
    print(C)

    stack = []
    for point in C:
        
        if stack and stack[-1][1] == point[1] and stack[-1][2]=='l' and point[2]=='r':
            stack.pop()
        else: 
            stack.append(point)
        print(stack)
    if stack:
        print("N0")
    else:
        print("YES")

    
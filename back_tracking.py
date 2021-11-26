'''
BackTracking
가능성이 없는 경우에는 일찍부터 차단해버리는 알고리즘, dfs랑 쓰인다!
'''
import sys
input  = sys.stdin.readline

# 15649

# N ,M = map(int,input().split())
# S = []

# def dfs():
    
#     if len(S) == M:
#         print(' '.join(map(str,S)))
#         return
    
#     for i in range(1, N+1):
#         if i not in S:
#             S.append(i)
#             dfs()
#             S.pop()
# dfs()


## 15650

# N ,M = map(int,input().split())
# S = []

# def dfs( lo ):
    
#     if len(S) == M:
#         print(' '.join(map(str,S)))
#         return
    
#     for i in range(lo, N+1):
#         if i not in S:
#             S.append(i)
#             dfs(i+1)
#             S.pop()
# dfs(1)

# 15651

# N ,M = map(int,input().split())
# S = []

# def dfs():
    
#     if len(S) == M:
#         print(' '.join(map(str,S)))
#         return
    
#     for i in range(1, N+1):
        
#         S.append(i)
#         dfs()
#         S.pop()
# dfs()


## 15652


# N ,M = map(int,input().split())
# S = []

# def dfs(lo):
    
#     if len(S) == M:
#         print(' '.join(map(str,S)))
#         return
    
#     for i in range(lo, N+1):
        
#         S.append(i)
#         dfs(i)
#         S.pop()
# dfs(1)

## 1182 
# N, S = map(int, input().split())
# arr = list(map(int, input().split()))
# nums = []
# cnt = 0 
# def dfs( i ):
#     global cnt 
#     if sum(nums) == S and nums:
#       cnt += 1
#     #   print(nums)
#     # return  쓰면안돼!! 다른 조합도 있을 수 있자나!
    
#     for j in range(i, len(arr)):
#         nums.append(arr[j])
#         dfs(j+1)
#         nums.pop()
# dfs(0)
# print(cnt)


## 6603

# def dfs(i):
#     if len(nums) == 6:
#         print(' '.join(map(str, nums)))
        
#     for j in range(i, len(S)):
#         nums.append(S[j])
#         dfs(j+1)
#         nums.pop()
# while True:
#     arr = list(map(int, input().split()))
#     k = arr[0]
#     if k == 0:
#         break
#     S = arr[1:]
#     nums = []
#     dfs(0)
#     print()
    
## 2661

# N = int(input())
# S = []
# cnt = 0
# def check_good(result, count):
#     for k in range(count):
#         stmp = result[k:]
#         for i in range(1, len(stmp)//2 +1):
#             if stmp[:i] == stmp[i: i+i]:
#                 return False
#     return True

# def dfs(cnt):
#     if S:
#         if not check_good(S,cnt):
            
#             return -1

#     if len(S) == N:
        
#         print(''.join(map(str,S)) )
#         return 0
   
#     for i in range(1,4):
#         S.append(i)
#         if dfs(cnt+1) == 0:
#             return 0
#         S.pop()
# dfs(0)


## 9663  N-Queens문제
# N = int(input())
# cnt = 0
# S = [0]*N

# def check(x):
#     for i in range(x):
#         if S[x] == S[i] or abs(S[x]-S[i]) == x-i:
#             return False
#     return True
    
        

# def dfs(x):
#     global cnt
    
#     if x == N:
#         cnt += 1
#         return
    
#     for i in range(0,N):
#         S[x] = i
#         if check(x):
#             dfs(x+1)
# dfs(0)
# print(cnt)   

### 아래식은 n-queens를 함수처럼 생각하며 풀어본 과정
# N = int(input())
# cnt = 0
# S = [0]*N

# def check(x,y):
#     for i in reversed(range(x)):
#         if y == S[i] or -i + x == abs(S[i]-y) : 
#             return False
#     # k_L = x + y
#     # k_R = -x + y
    
#     # for i in range(x):
#     #     if -i + k_L == S[i]:
#     #         return False
    
#     # for i in range(x):
#     #     if i + k_R == S[i]:
#     #         return False
    
#     return True
    
        

# def dfs(x):
#     global cnt
    
#     if x == N:
#         cnt += 1
#         return
    
#     for i in range(0,N):
#         S[x] = i
#         if check(x,i):
#             dfs(x+1)
# dfs(0)
# print(cnt)   



# 3580
sdk = []
for _ in range(9):
    sdk.append(list(map(int, input().split())))
    

problem =[(i,j) for i in range(9) for j in range(9) if sdk[i][j] == 0]
problem_num = len(problem)


part = [[0,1,2],[3,4,5],[6,7,8]]


def check(x,y,k):
    # 가로줄 체크
    for i in range(y):
        if sdk[x][i] == k:
            return False
    for i in range(y,9):
        if sdk[x][i] == k:
            return False
    # 세로줄 체크
    for j in range(x):
        if sdk[j][y] == k:
            return False
    for j in range(x,9):
        if sdk[j][y] == k:
            return False
    # 부분 사각형 체크
    for i in part[x//3]:
        for j in part[y//3]:
            if i == x and j ==y:
                continue
            if sdk[i][j] == k:
                return False
    return True


flag = False
def dfs(done):
    global flag
    if flag:
        return
    if done == problem_num:
        for i in range(9):
            print(*sdk[i])
            flag = True  
        return
    
    for k in range(1,10):
        if check(problem[done][0], problem[done][1],k):
            sdk[problem[done][0]][problem[done][1]] = k
            dfs(done+1)
            sdk[problem[done][0]][problem[done][1]] = 0
        
         
dfs(0)



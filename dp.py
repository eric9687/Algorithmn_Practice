import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# n = int(input())
# prev_ =list(map(int,input().split()))
# for _ in range(1,n):
#     new_ = list(map(int,input().split()))
#     new_[0] += prev_[0]
#     for i in range(1,len(new_)-1):
#         new_[i] = max(new_[i]+prev_[i-1],new_[i]+prev_[i])
#     new_[-1] += prev_[-1]
#     prev_ = new_

# print(max(prev_))

# n = int(input())
# dp = [ 0, 1, 2]

# for i in range(3,n+1):
#     dp.append(dp[i-1] + dp[i-2])
# print(dp[n]%10007)

# n = int(input())
# dp = [0,0,1,1]

# for i in range( 4, n+1 ):
#     dp.append(dp[i-1]+1)

#     if i % 2 == 0:
#         dp[i] = min (dp[i], dp[i//2]+1)
    
#     if i % 3 == 0:
#         dp[i] = min (dp[i], dp[i//3]+1)

# print(dp[n])

# n = int(input())

# arr = list(map(int, input().split()))
# dp = [0] * len(arr)
# dp[0] = arr[0]

# for i in range(1, len(arr)):
#     dp[i] = max(arr[i], dp[i-1] + arr[i])

# print(max(dp))


# def fibonacci(n):
#     zero_count = [1, 0]
#     one_count = [0, 1]

#     for i in range(2,n+1):
#         zero_count.append(zero_count[i-1] + zero_count[i-2])
#         one_count.append(one_count[i-1] + one_count[i-2])

#     print(zero_count[n], one_count[n])




# T = int(input())
# for _ in range(T):
#     fibonacci(int(input()))


# N = int(input())
# board = []
# for _ in range(N):
#     board.append(list(map(int,input().split())))
# count = 0

# dp=[[0]*N for _ in range(N)]
# dp[0][0]=1

# for x in range(N):
#     for y in range(N):
#         if y == N-1 and x == N-1:
#             break
#         elif dp[x][y] >= 1:
#             if 0 <= x+board[x][y] < N:
#                 dp[x+board[x][y]][y] += dp[x][y]
#             if 0 <= y+board[x][y] < N:
#                 dp[x][y+board[x][y]] += dp[x][y]

# print(dp[-1][-1])

N, K = map(int, input().split())
board = [[0]*(N+1) for _ in range(N+1)]
board[0][:] = [1]*(N+1)
for j in range(1,K):
    for i in range(1,N+1):
        if j==1:
            board[j][i] = 1
        else:
            board[j][i] = board[j-1][i] +board[j][i-1]
    
print(board)



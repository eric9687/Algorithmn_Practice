## 1629
# import sys
# input = sys.stdin.readline

# A, B, C = map(int,input().split())

# def Pow(x,n):
    
#     ret = 1
#     while n:
#         if n& 1 : ret =  ret * x % C
#         x *= x%C
#         n >>= 1
#     return ret 

# print(Pow(A,B))

# # def power(a,b):
# #     if b==1:
# #         return a%C
# #     else:
# #         temp = power(a,b//2)
# #         if b%2 == 0:
# #             return temp * temp % C
# #         else: return temp * temp * a % C
# # print(power(A,B))


## 1978
# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = list(map(int,input().split()))
# cnt = 0
# def isPrime(n):
#     if n <= 1 : return 0
#     for i in range(2,n+1):
#         if i*i > n: break
#         if n % i == 0: return 0
#     return 1
# for i in arr:
#     cnt += isPrime(i)
# print(cnt)

# def isPrime(n):
#     if n <= 1: return 0
#     for i in range(2,n+1):
#         if i*i > n: break
#         if n%i == 0: return


## 1929
# import sys
# input = sys.stdin.readline

# M,N = map(int, input().split())
# arr = range(N+1)
# result = []

# def Sieve(n):
#     sieve = [1]*(n+1)
#     sieve[0] = sieve[1] = 0
#     for i in range(2,n+1):
#         if i*i > n: break
#         if sieve[i]:
#             for j in range(i*i, n+1, i):
#                 sieve[j] = 0
#     return sieve

# sieve = Sieve(N)
# for i in range(M,N+1):
#     if sieve[i]:
#         print(i)


## 17425

def GetDivisor(n):
    ret = []
    for i in range(1,n+1):
        if i*i> n : break
        if n%i: continue
        ret.append(i)
        if i*i != n:ret.append(n//i)
    # ret.sort()
    return sum(ret)

def g(n):
    s=0
    for i in range(1, n+1):
        s += GetDivisor(i)
    return s

import sys
input =  sys.stdin.readline
MAX = 1000000
dp = [1] *(MAX+1)
S = [0] * (MAX+1)
for i in range(1, MAX+1):
    dp[i] = GetDivisor(i)
for i in range(2,MAX+1):
    S[i] = dp[i]+S[i-1]

for _ in range(int(input())):
    print(S[int(input())])



 
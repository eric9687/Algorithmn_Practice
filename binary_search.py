## 2805
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# tree = list(map(int,input().split()))
# lo, hi = 1, max(tree)

# while lo + 1 < hi:
#     mid = (lo+hi)//2
#     stick = 0 
#     for i in tree:
#         if i - mid > 0:
#             stick += i - mid
    
#     if stick < M:
#         hi = mid 
#     else:
#         lo = mid
# print(lo)

## 1654

# K,N = map(int, input().split())
# lan = []
# for _ in range(K):
#     lan.append(int(input()))
# lo, hi = 0, max(lan)+1

# while lo + 1 < hi:
#     mid = (lo + hi)//2
#     lines = 0
#     for l  in lan:
#         lines += l//mid
#     if lines < N:
#         hi = mid
#     else:
#         lo = mid
# print(lo)

## 2417
# n = int(input())
# lo, hi = 0 , n

# while lo + 1 < hi:
#     mid = (lo+hi)//2
#     if mid**2 >= n:
#         hi = mid
#     else:
#         lo = mid
# print(hi)

## 2792
# import sys
# input = sys.stdin.readline

# N,M =map(int,input().split())
# jwy = []
# for _ in range(M):
#     jwy.append(int(input()))
# lo, hi  = 1, max(jwy)

# while lo + 1 < hi:
#     mid  = (lo+hi)//2
#     total = 0    ## 학생수!!
#     for i in jwy:
#         st = i//mid if i%mid == 0 else i//mid + 1
#         total  += st
#     if total <= N :
#         hi = mid
#     else:
#         lo = mid
# print(hi)
    
    
## 2110
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house = sorted(house)
lo, hi = 1, 10**9+7   ### TTTTTFFFFF  lo와 hi는 무조건 T,F인 아이들로!!!

while lo + 1 < hi:
    mid = (lo + hi)//2
    
    cnt= 1
    cur_house = house[0]
    for i in range(1,N):
        if house[i] - cur_house >= mid:
            cnt += 1
            cur_house = house[i]
            
    if cnt < C:
        hi = mid
    else:
        lo = mid
        
print(lo)

## 10816
# import sys
# input = sys.stdin.readline

# N = int(input())
# card = list(map(int,input().split()))
# M = int(input())
# num = list(map(int,input().split()))
# dic = {}
# for c in card:
#     try:
#         dic[c] +=1
#     except:
#         dic[c] = 1
# result = []

# for nn in num:
#     try:
#         result.append(str(dic[nn]))
#     except:
#         result.append(str(0))

# print(' '.join(result))
# n = int(input())
# l, r = 0, n

# while l <= r:
#     m = (l+r)//2
#     if m**2 < n:
#         l = m + 1
#     else:
#         r = m-1
# if m**2 >= n:
#     print(m)
# else:
#     print(m+1)



####1654
# import sys
# K, N = map(int, input().split())
# lan =  [int(sys.stdin.readline()) for _ in range(K)]
# start, end = 1, max(lan)

# while start <= end:
#     mid = (start + end )//2
#     lines = 0
#     for l in lan:
#         lines += l // mid
    
#     if lines >= N:
#         start = mid +1
#     else:
#         end = mid -1

# print(end)

import sys
K, N = map(int, input().split())
lan =  [int(sys.stdin.readline()) for _ in range(K)]
lo, hi = 1, max(lan)

while lo +1 < hi:
    mid = (lo + hi )//2
    lines = 0
    for l in lan:
        lines += l // mid
    
    if lines < N:
        hi = mid
    else:
        lo = mid

print(lo)

# # 2805
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# tree =  list (map(int, input().split()))

# lo, hi = -1, max(tree)

# while lo +1 < hi:
#     mid = (lo + hi)//2

#     stick = 0
#     for tr in tree:
#         if tr - mid > 0:
#             stick += tr - mid
    
#     if stick < M : 
#         hi = mid
#     else:
#         lo = mid

# print(lo)


#2792
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# jry =  [int(sys.stdin.readline()) for _ in range(M)]

# lo, hi = -1, max(jry)

# while lo + 1 < hi:
#     mid = (lo + hi) // 2
#     jeal = 0
#     if mid ==0:
#         print(max(jry))
#         break
#     for i in jry:
#         jeal += i // mid
#         if i % mid > 0:
#             jeal += 1
#     if jeal <= N:
#         hi = mid
#     else:
#         lo = mid
# if mid != 0:
#     print(hi)


# import sys
# input = sys.stdin.readline
# M,N = map(int, input().split())
# t =  [int(sys.stdin.readline()) for _ in range(M)]

# lo, hi = 0, max(t)*N

# while lo + 1 < hi:
#     mid = (lo + hi) // 2
#     people = 0
#     for i in t:
#         people += mid// i
        
#     if people >= N:
#         hi = mid
#     else:
        
#         lo = mid

# print(hi)


# import sys
# input = sys.stdin.readline
# N, C = map(int, input().split())
# x =  [int(sys.stdin.readline()) for _ in range(N)]
# lo, hi = 1, max(x) - C +1

# while lo + 1 < hi:
#     mid = (lo + hi) // 2
#     wifi = 0
#     for xx in x:
#         wifi += mid // xx
#     if wifi < N:
#         hi = mid
#     else:
#         lo = mid

# print(lo)

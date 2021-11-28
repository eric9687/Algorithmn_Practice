# ## 2252
# import sys
# from collections import deque
# from collections import defaultdict
# input = sys.stdin.readline

# N, M = map(int, input().split())
# root =defaultdict(list)
# node = [0]*(N+1)
# queue = deque()
# answer= []

# for _ in range(M):
#     small, tall =  map(int,input().split())
#     root[small].append(tall)
#     node[tall] += 1

# for i in range(1,N+1):
#     if node[i] == 0:
#         queue.append(i)
# # print(queue)
# while queue:
#     student = queue.popleft()
#     answer.append(student)
#     for next_student in root[student]:
#         node[next_student] -= 1
#         if node[next_student] == 0:
#             queue.append(next_student)

# print(*answer)


## 2623
# import sys
# from collections import deque
# from collections import defaultdict
# input = sys.stdin.readline

# N, M = map(int, input().split())
# root =defaultdict(list)
# node = [0]*(N+1)
# queue = deque()
# answer= []

# for _ in range(M):
#     order = list( map(int,input().split()))
#     for i in range(1,order[0]):
#         root[order[i]].append(order[i+1])
#         node[order[i+1]] += 1


# for i in range(1,N+1):
#     if node[i] == 0:
#         queue.append(i)

# while queue:
#     student = queue.popleft()
#     answer.append(student)
#     for next_student in root[student]:
#         node[next_student] -= 1 
#         if node[next_student] == 0:
#             queue.append(next_student)
# if len(answer) != N:
#     print(0)
# else:
#     for i in answer:
#         print(i)


# ## 2056
# import sys
# from collections import deque
# from collections import defaultdict
# input = sys.stdin.readline

# N =  int(input())
# root =defaultdict(list)

# queue = deque()
# answer= []
# time = [0]*(N+1)

# for i in range(1,N+1):
#     order = list( map(int,input().split()))
#     time[i] = order[0]
#     for j in range(2,order[1]+2):
#         root[i].append(order[j])
        

# for  i in range(1,N+1):
#     temp = 0
#     for j in root[i]:
#         temp = max(temp,time[j])
#     time[i] += temp

# print(max(time))

## 1766

# import sys
# import heapq
# from collections import defaultdict
# input = sys.stdin.readline

# N, M = map(int, input().split())
# root =defaultdict(list)
# node = [0]*(N+1)
# heap = []
# answer= []

# for _ in range(M):
#     before, after =  map(int,input().split())
#     root[before].append(after)
#     node[after] += 1

# for i in range(1,N+1):
#     if node[i] == 0:
#         heapq.heappush(heap,i)




# while heap:
#     problem = heapq.heappop(heap)
#     answer.append(problem)
#     for next_problem in root[problem]:
#         node[next_problem] -= 1
#         if node[next_problem] == 0:
#             heapq.heappush(heap,next_problem)
    

# print(*answer)

## 3665
# import sys
# from collections import deque, defaultdict

# input  =  sys.stdin.readline

# for _ in range(int(input())):
#     N =  int(input())
#     order =  list(map(int,input().split()))
    
#     graph =  defaultdict(list)
#     node = [0] * (N+1)

#     for i in range(N-1):
#         for j in range(i+1,N):
#             graph[order[i]].append(order[j])
#             node[order[j]] += 1
    
#     for __ in range(int(input())):
#         i, j = map(int, input().split())
#         if i not in graph[j]:
#             tmp = i
#             i =j
#             j = tmp
#         graph[j].remove(i)
#         graph[i].append(j)
#         node[i] -= 1
#         node[j] += 1
        

#     queue = deque()
#     cnt = 0

#     for i in range(1,N+1):
#         if node[i] == 0:
#             queue.append(i)
#             cnt += 1
    
    
#     answer=[]
#     # if cnt > 1:
#     #     print("?")
#     # elif cnt == 0:
#     #     print("IMPOSSIBLE")
#     # else:
#     while queue:
#         now = queue.popleft()
#         answer.append(now)
#         for  i in graph[now]:
#             node[i] -= 1
#             if node[i] ==0 :
#                 queue.append(i)
#     if len(answer) != N:
#         print("IMPOSSIBLE")
#     else:
#         print(*answer)

## 1005
from collections import defaultdict, deque
import sys
input  = sys.stdin.readline

for _ in range(int(input())):
    graph = defaultdict(list)
    
    N, M = map(int,input().split())
    node = [0]*(N+1)
    time = [0]
    time= time+list(map(int,input().split()))
    duration = [0]*(N+1)
    for _ in range(M):
        before, after = map(int, input().split())
        graph[before].append(after)
        node[after] += 1
    queue = deque()
    for i in range(1,N+1):
        if node[i] == 0:
            queue.append(i)
            duration[i] = time[i]
    
    while queue:
        building = queue.popleft()
        for next_building in graph[building]:
            node[next_building] -= 1
            duration[next_building] = max(duration[building]+time[next_building], duration[next_building])
            if node[next_building] == 0:
                queue.append(next_building)
    answer = int(input())
    print(duration[answer])

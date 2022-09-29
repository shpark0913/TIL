'''
그래프 순회 :
    비선형구조인 그래프로 표현된 모든 자료(정점)를
    빠짐없이 탐색하는 것을 의미한다.
  ex) DFS(깊이우선탐색), BFS(넓이우선탐색)

  - 선형구조 : 자료 간의 관계가 1대1의 관계를 갖는다.
  - 비선형구조 : 자료 간의 관계가 1대N의 관계를 갖는다. (ex: 트리)
'''
# from collections import deque
#
# queue = deque()
#
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()
# print(queue)

################################################################

# def recursive_function():
#     print('재귀함수를 호출합니다')
#     recursive_function()
#
# recursive_function()

# def recursive_function(i):
#     if i == 100:
#         return
#     print(f'{i}번째 함수에서 {i+1}번째 함수를 호출합니다.')
#     recursive_function(i+1)
#     print(f'{i}번째 함수를 종료합니다.')
#
# recursive_function(1)

################################################################

# 반복문으로 구현한 factorial
# def factorial(n):
#     c = 1
#     for i in range(1, n+1):
#         c *= i
#     return c
#
# print(factorial(6))

# 재귀로 구현한 factorial
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)
#
# print(factorial(6))

################################################################

# 인접 행렬 예제
# INF = 99999999
# graph = [
#     [0, 7, 5],
#     [7, 0, INF],
#     [5, INF, 0]
# ]

# 인접 리스트
# graph = [[] for _ in range(3)]
# graph[0].append((1, 7))
# graph[0].append((2, 5))
# graph[1].append((0, 7))
# graph[2].append((0, 5))
# print(graph)


################################################################


# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
#
# visited = [False] * len(graph)

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end = ' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
# dfs(graph, 1, visited)


# from collections import deque
#
# def bfs(graph, v, visited):
#     queue = deque([v])
#     visited[v] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end = ' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
#
# bfs(graph, 1, visited)

################################################################

# 음료수 얼려 먹기

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

# N, M = map(int, input().split())                    # N : 행의 개수 / M : 열의 개수
#
# ice = [list(map(int, input())) for _ in range(N)]   # 현재 얼음의 분포

# def dfs(x, y):
#     if x < 0 or x >= N or y < 0 or y >= M:
#         return False                                # 얼음판 벗어나면 False
#
#     if ice[x][y] == 0:                              # 얼음판 0이면
#         ice[x][y] = 1                               # 1로 바꾸고
#         dfs(x-1, y)                                 # 상하좌우 탐색하며 0인 친구들 1로 바꿔주기
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False
#
# res = 0
#
# for i in range(N):
#     for j in range(M):
#         if dfs(i, j) == True:
#             res += 1
#
# print(res)


################################################################

# 미로 탈출

'''
5 6
101010
111111
000001
111111
111111
'''
# from collections import deque
#
# N, M = map(int, input().split())
# graph = [list(map(int, input())) for _ in range(N)]
#
# dx = [-1, 1, 0, 0]                                     # 상하좌우
# dy = [0, 0, -1, 1]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= N or ny >= M:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     return graph[N-1][M-1]
#
# print(bfs(0, 0))
# print(graph)

################################################################

# Q.15 : 특정 거리의 도시 찾기

''' 답 : 4
4 4 2 1 
1 2
1 3
2 3
2 4
'''

''' 답 : -1
4 3 2 1
1 2
1 3
1 4
'''

''' 답 : 2 /n 3
4 4 1 1 
1 2 
1 3
2 3
2 4
'''


# from collections import deque
#
# N, M, K, X = map(int, input().split())      # N : 도시 수 / M : 도로 수 / X 도시로부터 최단 거리가 K인 도시를 찾아라!!
#
# graph = [[] for _ in range(N+1)]            # 단방향 연결리스트
# visited = [0] * (N+1)
# for i in range(M):
#     s, e = map(int,input().split())
#     graph[s].append(e)
# cnt = 0
#
# def bfs(x):
#     global cnt
#     queue = deque()
#     queue.append(x)
#     visited[x] = cnt
#     while queue:
#         x = queue.popleft()
#         cnt += 1
#         for i in graph[x]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = cnt
#
# bfs(X)
# lst = []
# for i in range(len(visited)):
#     if visited[i] == K:
#         lst.append(i)
# if lst:
#     for elt in lst:
#         print(elt)
# else:
#     print(-1)

################################################################













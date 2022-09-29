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


from collections import deque

N, M, K, X = map(int, input().split())      # N : 도시 수 / M : 도로 수 / X 도시로부터 최단 거리가 K인 도시를 찾아라!!

graph = [[] for _ in range(N+1)]            # 단방향 연결리스트
visited = [0] * (N+1)
for i in range(M):
    s, e = map(int,input().split())
    graph[s].append(e)
cnt = 0

def bfs(x):
    global cnt
    queue = deque()
    queue.append(x)
    visited[x] = cnt
    while queue:
        x = queue.popleft()
        cnt += 1
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = cnt

bfs(X)
lst = []
for i in range(len(visited)):
    if visited[i] == K:
        lst.append(i)
if lst:
    for elt in lst:
        print(elt)
else:
    print(-1)
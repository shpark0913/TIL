'''
마지막 정점 번호(0번부터 시작) / 간선의 수
6 8
0 1 0 2 0 5 0 6 4 3 5 3 6 4 5 4
'''

# 인접 행렬, 인접 리스트 만들기

V, E = map(int,input().split())
arr = list(map(int,input().split()))

adjM = [[0] * (V+1) for _ in range(V+1)]   # 인접 행렬
adjList = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2 + 1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1        # 방향이 없는 경우에만

    adjList[n1].append(n2)
    adjList[n2].append(n1)  # 방향이 있는 경우에만

print(adjM)
print(adjList)
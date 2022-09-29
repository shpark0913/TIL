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

N, M = map(int, input().split())                    # N : 행의 개수 / M : 열의 개수

ice = [list(map(int, input())) for _ in range(N)]   # 현재 얼음의 분포

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False                                # 얼음판 벗어나면 False

    if ice[x][y] == 0:                              # 얼음판 0이면
        ice[x][y] = 1                               # 1로 바꾸고
        dfs(x-1, y)                                 # 상하좌우 탐색하며 0인 친구들 1로 바꿔주기
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

res = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            res += 1

print(res)

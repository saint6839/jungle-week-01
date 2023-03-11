import sys

sys.setrecursionlimit(1000000)
M, N, K = map(int, sys.stdin.readline().split())

maps = [[0 for i in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            maps[j][i] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    global cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and not maps[nx][ny]:
            cnt += 1
            maps[nx][ny] = 1
            dfs(nx, ny)
area = 0
cnt = 1
results =[]
for i in range(N):
    for j in range(M):
        if not maps[j][i]:
            area += 1
            maps[j][i] = 1
            dfs(j, i)
            results.append(cnt)
            cnt = 1

results.sort()
print(area)
print(' '.join(map(str, results)))
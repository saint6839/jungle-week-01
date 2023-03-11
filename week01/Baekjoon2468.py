import sys
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())

maps = []

for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

max_value = max(max(row) for row in maps)

result = -sys.maxsize



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, height):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N):
            if maps[nx][ny] > height and isVisits[nx][ny] == 0:
                isVisits[nx][ny] = True
                dfs(nx, ny, height)

for i in range(max_value):
    count = 0
    isVisits = [[False for _ in range(N)] for _ in range(N)]

    for j in range(N):
        for k in range(N):
            if maps[j][k] > i and not isVisits[j][k]:
                isVisits[j][k] = True
                count += 1
                dfs(j, k, i)

    result = max(result, count)

print(result)



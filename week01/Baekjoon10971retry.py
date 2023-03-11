import sys

N = int(sys.stdin.readline())

maps = []

for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

isVisits = [False for i in range(N)]

min = sys.maxsize

def dfs(x, y, value, depth):
    global min

    if depth == N-1:
        if maps[y][x]:
            value += maps[y][x]
            if min > value:
                min = value
            return

    for i in range(N):
        if not isVisits[i] and maps[y][i]:
            isVisits[i] = True
            dfs(x, i, value + maps[y][i], depth+1)
            isVisits[i] = False

for i in range(N):
    isVisits[i] = True
    dfs(i, i, 0, 0)
    isVisits[i] = False

print(min)
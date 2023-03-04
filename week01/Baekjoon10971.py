import sys

N = int(sys.stdin.readline())

matrix = []
isVisits = [False for i in range(N)]

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

min = sys.maxsize

def dfs(start, now, value, cnt):
    global min
    if cnt == N-1:
        if matrix[now][start]:
            value += matrix[now][start]
            if min > value:
                min = value
            return

    if min < value:
        return

    for i in range(N):
        if not isVisits[i] and matrix[now][i]:
            isVisits[i] = True
            dfs(start, i, value + matrix[now][i], cnt + 1)
            isVisits[i] = False

for i in range(N):
    isVisits[i] = True
    dfs(i, i, 0, 0)
    isVisits[i] = False

print(min)
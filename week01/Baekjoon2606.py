import sys

N = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

pairs = [[False for i in range(N+1)] for _ in range(N+1)]

for _ in range(pair):
    start, end = map(int, sys.stdin.readline().split())
    pairs[start][end] = True
    pairs[end][start] = True

isVisits = [False for i in range(N+1)]

result = 0
def dfs(start):
    global result
    isVisits[start] = True

    for i in range(1, len(pairs)):
        if pairs[start][i] and not isVisits[i]:
            result += 1
            dfs(i)

dfs(1)
print(result)

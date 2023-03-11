import sys

N, M = map(int, sys.stdin.readline().split())

temps = []
def dfs(depth, index):
    if depth == M:
        for temp in temps:
            print(temp, end=' ')
        print()
        return

    for i in range(index, N+1):
        if not temps.__contains__(i):
            temps.append(i)
            dfs(depth+1, i)
            temps.pop()

dfs(0, 1)
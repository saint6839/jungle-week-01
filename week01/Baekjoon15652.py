import sys

N, M = map(int, sys.stdin.readline().split())

temps = []


def dfs(depth, index):
    if depth == M:
        print(' '.join(map(str, temps)))
        return

    for i in range(index, N + 1):
        temps.append(i)
        dfs(depth + 1, i)
        temps.pop()


dfs(0, 1)

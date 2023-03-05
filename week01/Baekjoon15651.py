import sys

N, M = map(int, sys.stdin.readline().split())


temps = []
def dfs(depth):
    if depth == M:
        for temp in temps:
            print(temp, end=' ')
        print()
        return

    for i in range(1, N+1):
        temps.append(i)
        dfs(depth+1)
        temps.pop()


dfs(0)
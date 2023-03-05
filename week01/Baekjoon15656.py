import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

temps = []

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, temps)))
        return

    for i in range(N):
        temps.append(numbers[i])
        dfs(depth+1)
        temps.pop()

dfs(0)


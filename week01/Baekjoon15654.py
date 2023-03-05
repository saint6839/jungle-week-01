import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

temps = []

def dfs(depth, index):
    if depth==M:
        print(' '.join(map(str, temps)))
        return

    for i in range(N):
        if not numbers[i] in temps:
            temps.append(numbers[i])
            dfs(depth+1, i)
            temps.pop()

dfs(0, 0)




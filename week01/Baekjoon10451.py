import sys

T = int(sys.stdin.readline())


def dfs(start, isVisits):
    isVisits[start] = True
    next = numbers[start]
    if not isVisits[next]:
        dfs(next, isVisits)


for _ in range(T):
    N = int(sys.stdin.readline())
    numbers = [0] + list(map(int, sys.stdin.readline().split()))

    result = 0
    isVisits = [0] + [False for _ in range(N + 1)]
    for i in range(1, N+1):
        if not isVisits[i]:
            dfs(i, isVisits)
            result += 1

    print(result)



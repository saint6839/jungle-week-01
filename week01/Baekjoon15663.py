import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()
temps = []

results = set()

isVisits = [False for i in range(N)]

def dfs(depth):
    if depth == M:
        results.add(tuple(temps))
        return

    for i in range(N):
        if not isVisits[i]:
            isVisits[i] = True
            temps.append(numbers[i])
            dfs(depth+1)
            temps.pop()
            isVisits[i] = False

dfs(0)

results = list(map(list,results))
results.sort()
for result in results:
    for r in result:
        print(r, end=' ')
    print()


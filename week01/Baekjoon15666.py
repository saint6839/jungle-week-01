import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()
temps = []


isVisits = [False for i in range(N)]
results = set()

def dfs(depth, index):
    if depth == M:
        results.add(tuple(temps))
        return

    for i in range(index, N):
        temps.append(numbers[i])
        dfs(depth+1, i)
        temps.pop()

dfs(0,0)

results = list(map(list,results))
results.sort()
for result in results:
    for r in result:
        print(r, end=' ')
    print()
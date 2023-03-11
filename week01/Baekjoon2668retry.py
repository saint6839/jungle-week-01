import sys

N = int(sys.stdin.readline())

connections = [0 for i in range(N+1)]

isVisits = [False] * (N + 1)
results = set()

def dfs(start, x):
    temps.append(x)
    if connections[x] == start:
        temps.sort()
        results.add(tuple(temps))
        return

    if not isVisits[connections[x]]:
        isVisits[connections[x]] = True
        dfs(start, connections[x])

    isVisits[connections[x]] = False

for i in range(1, N+1):
    connections[i] = int(sys.stdin.readline())


for i in range(1, N+1):
    if not isVisits[i]:
        isVisits[i] = True
        temps = []
        dfs(i, i)

real_results = []

for i in results:
    for j in i:
        real_results.append(j)

real_results.sort()
print(len(real_results))
print(*real_results, sep="\n")



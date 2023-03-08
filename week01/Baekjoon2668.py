import sys

N = int(sys.stdin.readline())


connections = [[] for i in range(N+1)]

for i in range(1, N+1):
    connections[i].append(int(sys.stdin.readline()))

def dfs(num):
    if not isVisits[num]:
        isVisits[num] = True
        for connection in connections[num]:
            first.add(num)
            second.add(connection)

            if first == second:
                results.extend(list(second))
                return
            dfs(connection)
    isVisits[num] = False

results = []

for i in range(1, N+1):
    isVisits = [False] * (N + 1)
    first = set()
    second = set()

    dfs(i)

results = list(set(results))
results.sort()

print(len(results))
print(*results, sep="\n")


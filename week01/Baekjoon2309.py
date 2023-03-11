import sys

isVisits = [False for i in range(9)]
heights = []
results = []

for _ in range(9):
    heights.append(int(sys.stdin.readline()))


def dfs(cnt, start):
    if cnt == 7 and sum(results) == 100:
        results.sort()
        for result in results:
            print(result)
        exit(0)

    for i in range(9):
        if not isVisits[i]:
            isVisits[i] = True
            results.append(heights[i])
            dfs(cnt + 1, i)
            isVisits[i] = False
            results.pop()

dfs(0, 0)

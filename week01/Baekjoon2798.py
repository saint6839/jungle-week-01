import sys

N, M = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))
isVisits = [False for i in range(N)]

max = 0
def dfs(sum, count, start):
    global max
    if sum > M:
        return
    if count == 3 and sum <= M:
        if max < sum:
            max = sum
        return

    for i in range(start, N):
        if not isVisits[i]:
            isVisits[i] = True
            dfs(sum + numbers[i], count + 1, i+1)
            isVisits[i] = False

dfs(0, 0, 0)

sys.stdout.write(str(max))

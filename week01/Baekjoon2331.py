import sys

A, P = map(int, sys.stdin.readline().split())

D = [0] + [A]

checks = [0] * 250000
count = 0

def dfs(value):
    global count
    if checks[value]:
        print(checks[value] - 1)
        return
    count += 1
    checks[value] = count

    temp = 0
    for s in str(value):
        temp += int(s) ** P

    return dfs(temp)

dfs(D[1])

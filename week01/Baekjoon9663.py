import sys

N = int(sys.stdin.readline())

row = [0] * N

result = 0

def can_put(column):
    for i in range(column):
        if row[column] == row[i] or abs(row[column] - row[i]) == abs(column - i):
            return False
    return True

def dfs(column):
    global result

    if column == N:
        result += 1
        return

    for i in range(N):
        row[column] = i
        if can_put(column):
            dfs(column + 1)

dfs(0)
print(result)

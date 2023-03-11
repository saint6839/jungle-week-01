import sys

N = int(sys.stdin.readline())

row = [0] * N
isVisits = [[False for _ in range(N)] for _ in range(N)]
result = 0

def can_put(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def n_queens(x):
    global result
    if x == N:
        result += 1
        return

    for i in range(N):
        row[x] = i
        if can_put(x):
            if not isVisits[x][i]:
                isVisits[x][i] = True
                n_queens(x+1)
                isVisits[x][i] = False

n_queens(0)
sys.stdout.write(str(result))
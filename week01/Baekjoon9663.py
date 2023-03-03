import sys

N = int(sys.stdin.readline())

map = [0] * N
result = 0

def can_put(x):
    for i in range(x):
        if map[x] == map[i] or abs(map[x] - map[i]) == abs(x - i):
            return False
    return True

def recursive(x):
    global result
    if x == N:
        result += 1
        return

    for i in range(N):
        map[x] = i
        if can_put(x):
            recursive(x + 1)

recursive(0)
print(result)
import sys

result = 0

maps = [[False for i in range(100)] for _ in range(100)]

for i in range(4):
    xl, yl, xr, yr = map(int, sys.stdin.readline().split())

    for i in range(xl, xr):
        for j in range(yl, yr):
            if not maps[i][j]:
                maps[i][j] = True
                result+=1

print(result)

import sys

N = int(sys.stdin.readline())

given = list(map(int, sys.stdin.readline().split()))

nx = 0
ny = 0
positions = []
for i in given:
    if i == 1:
        nx += 1
        positions.append([nx, ny])
    if i == 2:
        ny += 1
        positions.append([nx, ny])
    if i == 3:
        nx -= 1
        positions.append([nx, ny])
    if i == 4:
        ny -= 1
        positions.append([nx, ny])

T = int(sys.stdin.readline())

results = []

positions.sort()

for _ in range(T):
    cases = list(map(int, sys.stdin.readline().split()))
    t_nx = 0
    t_ny = 0
    temps = []
    for i in cases:
        if i == 1:
            t_nx += 1
            temps.append([t_nx, t_ny])
        if i == 2:
            t_ny += 1
            temps.append([t_nx, t_ny])
        if i == 3:
            t_nx -= 1
            temps.append([t_nx, t_ny])
        if i == 4:
            t_ny -= 1
            temps.append([t_nx, t_ny])

    temps.sort()

    diff_x = positions[0][0] - temps[0][0]
    diff_y = positions[0][1] - temps[0][1]

    isSame = True
    for i in range(len(positions)):
        temps[i][0] += diff_x
        temps[i][1] += diff_y

        if temps[i][0] != positions[i][0] or temps[i][1] != positions[i][1]:
            isSame = False
            break

    if isSame:
        results.append(cases)


print(len(results))
for result in results:
    for r in result:
        print(r, end=' ')
    print()


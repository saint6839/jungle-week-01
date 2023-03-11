import sys

width, length = map(int, sys.stdin.readline().split())

N = int(sys.stdin.readline())

width_cut = [0]
length_cut = [0]

for _ in range(N):
    dir, pos = map(int, sys.stdin.readline().split())
    if dir == 0:
        width_cut.append(pos)
    else:
        length_cut.append(pos)

width_cut.append(length)
length_cut.append(width)

width_cut.sort()
length_cut.sort()
max_width_diff = 0
for i in range(0, len(width_cut)-1):
    diff = width_cut[i+1] - width_cut[i]
    if max_width_diff < diff:
        max_width_diff = diff

max_length_diff = 0
for i in range(0, len(length_cut)-1):
    diff = length_cut[i+1] - length_cut[i]
    if max_length_diff < diff:
        max_length_diff = diff
print(max_width_diff * max_length_diff)

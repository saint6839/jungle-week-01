import sys

N = int(sys.stdin.readline())

counts = [0 for i in range(10001)]

max = 0
for _ in range(N):
    value = int(sys.stdin.readline())
    if max < value:
        max = value
    counts[value] += 1
for i in range(max+1):
    while(counts[i] > 0):
        print(i)
        counts[i] -= 1

A = int(input())
B = int(input())
C = int(input())

counts = list()

for i in range(10):
    counts.append(0)

values = str(A * B * C)

for value in values:
    counts[int(value)] += 1

for count in counts:
    print(count)

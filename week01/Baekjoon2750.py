import sys

N = int(sys.stdin.readline())

numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for number in numbers:
    print(number)

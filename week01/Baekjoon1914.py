import sys

N = int(sys.stdin.readline())

results = list()

print(2**N - 1)
def move(no, x, y):
    if no > 1:
        move(no - 1, x, 6-x-y)

    print(x, y)

    if no > 1:
        move(no - 1, 6-x-y, y)
if N<= 20:
    move(N, 1, 3)

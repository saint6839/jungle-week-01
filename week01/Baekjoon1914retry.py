import sys

N = int(sys.stdin.readline())

print(2**N - 1)

def move(n, a, c, b):
    if n == 0:
        return

    move(n-1, a, b, c)
    print(a, c)
    move(n-1, b, c, a)

if N<=20:
    move(N,1,3,2)
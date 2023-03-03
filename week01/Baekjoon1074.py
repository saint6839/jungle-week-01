import sys

N, r, c = map(int, sys.stdin.readline().split())
cnt = 0


def recurive(x, y, n):
    global cnt
    if x == r and y == c:
        print(cnt)
        exit(0)

    if n == 1:
        cnt += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        cnt += n * n
        return

    recurive(x, y, n/2)
    recurive(x, y+n/2, n/2)
    recurive(x+n/2, y, n/2)
    recurive(x+n/2, y+n/2, n/2)


recurive(0, 0, 2 ** N)
print(cnt)

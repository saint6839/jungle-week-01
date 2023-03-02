N, X = map(int, input().split())

A = list(map(int, input().split()))

for a in A:
    if X > int(a):
        print(a, end=' ')
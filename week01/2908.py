import sys
a, b = map(int, sys.stdin.readline().split())

def reverse(num):
    
    res = 0
    while num > 0:
        tmp = num % 10
        res *= 10
        res += tmp
        num = num //10

    return res

print(max(reverse(a), reverse(b)))

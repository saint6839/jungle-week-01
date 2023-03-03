"""
구구단
"""
import sys

n = int(sys.stdin.readline().rstrip())
for i in range(1, 10):
    print("%d * %d = %d" % (n, i, i*n))
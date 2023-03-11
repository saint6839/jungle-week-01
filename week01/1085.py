"""
직사각형에서 탈출
"""
import sys

x, y, w, h = map(int, sys.stdin.readline().split())

a = min(x, abs(w-x))
b = min(y, abs(y-h))
print(min(a, b))
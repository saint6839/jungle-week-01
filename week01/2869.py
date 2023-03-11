import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

cnt1 = (v-a) / (a-b)
print(math.ceil(cnt1)+1)
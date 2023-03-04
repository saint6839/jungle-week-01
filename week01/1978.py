import sys
import math
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")

n = int(sys.stdin.readline().rstrip())
ls = [int(x) for x in sys.stdin.readline().split()]

maxi = max(ls)
print(maxi)
ch = [0] * (maxi+1)
ch[0], ch[1] = 1, 1    
for i in range(2, math.sqrt(maxi)+1):
    if ch[i] == 0:
        for j in range(i*i, maxi+1, i):
            ch[j] = 1

cnt = 0
for x in ls:
    if ch[x] == 0:
        cnt += 1

print(cnt)
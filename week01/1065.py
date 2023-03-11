import sys
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")

n = int(sys.stdin.readline().rstrip())

cnt = 0
if n < 100:
    cnt = n
else:
    cnt = 99
    for num in range(100, n+1):
        ls = [int(x) for x in list(str(num))]
        if (ls[0]-ls[1]) == (ls[1]-ls[2]):
            cnt += 1

print(cnt)
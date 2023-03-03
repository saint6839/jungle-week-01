import sys
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")


n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    ls = list(map(int, sys.stdin.readline().split()))
    avg = sum(ls[1:])/ls[0]
    count = len([x for x in ls[1:] if x > avg])
    print('{:.3f}%'.format(count/ls[0]*100))
    
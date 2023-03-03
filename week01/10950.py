import sys
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a, b = map(int, (sys.stdin.readline().rstrip()).split())
    print(a+b)
import sys
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a, word = sys.stdin.readline().split()
    for s in word:
        print(s * int(a), end='')
    print()    
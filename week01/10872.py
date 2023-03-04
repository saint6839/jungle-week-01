import sys
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")

n = int(sys.stdin.readline().rstrip())

def func(n):
    if n == 0:
        return 1
    else:
        return n * func(n-1)
    
print(func(n))
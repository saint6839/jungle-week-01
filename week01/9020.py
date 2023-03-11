import sys
import math
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    mid = n//2
    for i in range(mid+1, 1, -1):
        if is_prime(i):
            if is_prime(n-i):
                if i < n-i:
                    print(i, n-i)
                else:
                    print(n-i, i)
                break
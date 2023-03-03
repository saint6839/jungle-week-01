import sys
# import os.path

# scriptpath = os.path.dirname(__file__)
# filename = os.path.join(scriptpath, 'input.txt')
# sys.stdin = open(filename, "rt")

"""
X보다 작은 수
"""
n, maxi = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))
for i in ls:
    if i < maxi:
        print(i, end=' ')

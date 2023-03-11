import sys
# import os.path

# scriptpath = os.path.dirname(__file__)
# filename = os.path.join(scriptpath, 'input.txt')
# sys.stdin = open(filename, "rt")

"""
별찍기
"""

n = int(sys.stdin.readline().rstrip())
for i in range(1, n+1):
    print("*" * i)
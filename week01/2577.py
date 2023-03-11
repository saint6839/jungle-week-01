import sys
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")

"""
숫자의 개수
"""
tot = 1
for _ in range(3):
    tot *= int(sys.stdin.readline().rstrip())

ls = [0] * 10
for i in str(tot):
    ls[int(i)] += 1

for j in ls:
    print(j)

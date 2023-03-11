import sys
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")

w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline().rstrip())

x_ls = [0, w]
y_ls = [0, h]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        x_ls.append(b)
    else:
        y_ls.append(b)

x_ls.sort()
y_ls.sort()
print(x_ls, y_ls)

width_ls = list()
height_ls = list()
for i in range(1, len(x_ls)):
    width_ls.append(x_ls[i]-x_ls[i-1])

for j in range(1, len(y_ls)):
    height_ls.append(y_ls[j]-y_ls[j-1])

print(max(width_ls) * max(height_ls))
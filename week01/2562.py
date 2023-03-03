import sys
# import os.path

# scriptpath = os.path.dirname(__file__)
# filename = os.path.join(scriptpath, 'input.txt')
# sys.stdin = open(filename, "rt")

idx = 0
maxi = -float('inf')
for i in range(1, 10):
    n = int(sys.stdin.readline().rstrip())
    if n > maxi:
        maxi = n
        idx = i

print(maxi)
print(idx)
    

import sys
# import os.path

# scriptpath = os.path.dirname(__file__)
# filename = os.path.join(scriptpath, 'input.txt')
# sys.stdin = open(filename, "rt")


n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    score = 1
    tot = 0
    for ox in line:
        if ox == 'O':
            tot += score
            score += 1
        else:
            score = 1
    else:
        print(tot)

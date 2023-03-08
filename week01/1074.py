import sys
import math
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")


def get_target(a, x, y, tot, target):
    if a == 1:
        target = 2*x + y
        return a, x, y, tot+a*a*target, target
    else:
        if x >= a:
            if y >= a:
                target = 3
                x = x - a
                y = y - a
            else:
                target = 2
                x = x - a
        else:
            if y >= a:
                target = 1
                y = y - a
            else:
                target = 0

        return get_target(a//2, x, y, tot+a*a*target, target)


if __name__ == '__main__':
    n, r, c = map(int, sys.stdin.readline().split())
    a = 2**(n-1)
    a, x, y, tot, target = get_target(a, r, c, 0, 0)
    print(tot)
        


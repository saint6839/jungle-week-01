import sys
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'input.txt')
sys.stdin = open(filename, "rt")


def func(L, num):
    if L == k:
        sett.add(num)
        return
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                func(L+1, num + str(ls[i]))
                ch[i] = 0


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline().rstrip())
    ls = [int(sys.stdin.readline()) for _ in range(n)]
    
    sett = set()
    ch = [0] * n
    for i in range(n):
        ch[i] = 1
        func(1, str(ls[i]))
        ch[i] = 0

    print(len(sett))
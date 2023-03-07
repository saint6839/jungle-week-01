import sys

board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(9)]
empties = []

def colCheck(num, c):
    for r in range(9):
        if board[r][c] == num:
            return False
    return True

def rowCheck(num, r):
    for c in range(9):
        if board[r][c] == num:
            return False
    return True

def squareCheck(num, r, c):
    nr = (r//3) * 3
    nc = (c//3) * 3
    for i in range(3):
        for j in range(3):
            if board[nr + i][nc + j] == num:
                return False
    return True

def dfs(depth):
    if depth == len(empties):
        for row in range(9):
            for col in range(9):
                print(board[row][col], end="")
            print()
        exit(0)

    nr, nc = empties[depth]
    for i in range(1, 10):
        if colCheck(i, nc) and rowCheck(i, nr) and squareCheck(i, nr, nc):
            board[nr][nc] = i
            dfs(depth+1)
            board[nr][nc] = 0

for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            empties.append((r, c))

dfs(0)
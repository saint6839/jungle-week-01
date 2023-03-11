import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

dRow = [-1, 0, 1 ,0]
dCol = [0, -1, 0, 1]

def dfs(row, col):
    board[row][col] = 0
    for i in range(4):
        nRow = row + dRow[i]
        nCol = col + dCol[i]

        if 0 <= nRow < N and 0 <= nCol < M and board[nRow][nCol]:
            dfs(nRow, nCol)

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[0 for i in range(M)] for _ in range(N)]
    for _ in range(K):
        col, row = map(int, sys.stdin.readline().split())
        board[row][col] = 1

    count = 0

    for col in range(M):
        for row in range(N):
            if board[row][col]:
                board[row][col] = 0
                count += 1
                dfs(row, col)

    print(count)

    # for i in range(M):
    #     for j in  range(N):
    #         print(board[j][i], end=' ')
    #     print()


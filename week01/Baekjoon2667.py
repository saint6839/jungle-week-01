import sys

N = int(sys.stdin.readline())

board = [list(map(int, list(str(sys.stdin.readline().strip())))) for _ in range(N)]
# print(board)
# for i in range(N):
#     for j in range(N):
#         print(board[i][j], end=' ')
#     print()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    global count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
            count += 1
            board[nx][ny] = 0
            dfs(nx, ny)


counts = []
total = 0
for i in range(N):
    for j in range(N):
        count = 0
        if board[i][j]:
            board[i][j] = 0
            count += 1
            total += 1
            dfs(i, j)
            counts.append(count)

print(total)
counts.sort()
print(*counts, sep='\n')

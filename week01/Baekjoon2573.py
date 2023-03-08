import sys

sys.setrecursionlimit(10 ** 5)


def dfs(row, col):  # 2가지 경우로 나뉘는걸 체크해주기 위한 함수.
    for k in range(4):
        nRow = dRow[k] + row
        nCol = dCol[k] + col
        if 0 <= nRow < N and 0 <= nCol < M and isVisits[nRow][nCol]:
            isVisits[nRow][nCol] = False
            if board[nRow][nCol] != 0:
                dfs(nRow, nCol)


input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dRow = [1, -1, 0, 0]
dCol = [0, 0, 1, -1]
isVisits = [[False] * M for _ in range(N)]  # 방문 체크
area = 0

while True:
    area += 1
    for i in range(N):  # 빙하를 녹이는 함수
        for j in range(M):
            if board[i][j] != 0:
                isVisits[i][j] = True  # 앞서 말한 경우를 방지해주기 위한 작업
                ice = board[i][j]
                for k in range(4):
                    nx = dRow[k] + i
                    ny = dCol[k] + j
                    if 0 <= nx < N and 0 <= ny < M and not isVisits[nx][ny]:
                        if board[nx][ny] == 0:
                            ice -= 1
                            if ice == 0:  # 음수가 되면 안 되니 dfs작업을 멈춰준다.
                                break
                board[i][j] = ice  # 녹은 빙하를 저장해줌

    ch = 0  # 영역의 개수
    for i in range(N):
        for j in range(M):  # 방문체크 배열을 재사용하기 위해 True->False로 다 고쳐준다.
            if board[i][j] != 0 and isVisits[i][j]:
                dfs(i, j)  # 영역을 체크한다.
                ch += 1
            elif board[i][j] == 0 and isVisits[i][j]:
                isVisits[i][j] = False

    if ch >= 2:  # 영역이 2개 이상으로 나뉜경우니 출력해주고 반복문을 탈출한다.
        print(area)
        break
    elif ch == 0:  # 한번에 녹았다는 의미이므로 0을 출력해주고 반복문을 탈출한다.
        print(0)
        break
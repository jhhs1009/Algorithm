'''
로봇 청소기
고친 버전
'''

from collections import deque

# 12, 3, 6, 9 시 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def b(r, c, d):
    cnt = 0
    q = deque()
    q.append((r, c, d))

    while q:
        flag = 0
        r, c, d = q.popleft()

        # 현재 위치 청소
        if board[r][c] == 0:
            board[r][c] = 3
            cnt += 1

        for i in range(1, 5):
            nr, nc = r + dr[(d - i )], c + dc[(d - i ) ]
            # 청소되지 않은 빈칸이 있는 경우
            if board[nr][nc] == 0:
                flag += 1
                # 회전했고 청소 되지 않은 빈칸
                q.append((nr, nc, (d - i + 4) % 4))
                break
        # 청소되지 않은 빈칸이 없는 경우
        while flag == 0:
            if d == 0:
                d = 2
                nr = r + dr[d]
                nc = c + dc[d]
                d = 0
            elif d == 2:
                d = 0
                nr = r + dr[d]
                nc = c + dc[d]
                d = 2
            elif d == 1:
                d = 3
                nr = r + dr[d]
                nc = c + dc[d]
                d = 1
            elif d == 3:
                d = 1
                nr = r + dr[d]
                nc = c + dc[d]
                d = 3

            if board[nr][nc] != 1:
                q.append((nr, nc, d))
                break
            elif board[nr][nc] == 1:
                return cnt


n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(b(r, c, d))
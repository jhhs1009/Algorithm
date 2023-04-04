'''
로봇 청소기
로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오

N*M 크기의 직사각형으로 나타낼 수 있음
칸 = 벽 or 빈 칸

0,0 -> N-1,M-1

1. 현재 칸이 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸중 청소되지 않은 빈 칸이 없는 경우
    - 바라보는 방향 유지, 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아감
    - 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동 중지
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    - 반시계 방향, 90도 회전 ( 왼쪽 )
    - 바라보는 방향을 기준, 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
    - 1번으로 돌아감

북동남서 상우하좌

처음 빈칸은 전부 청소되지 않은 상태
'''
from collections import deque

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def b(r,c,d):
    global cnt
    q = deque()
    q.append((r,c,d))
    board[r][c] = 3

    while q:
        flag = 0
        r,c,d = q.popleft()

        # 현재 위치 청소
        if board[r][c] == 0:
            board[r][c] = 3

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<n and 0<=nc<m:
                # 청소되지 않은 빈칸이 있는 경우
                if board[nr][nc] == 0:
                    flag += 1
                    # 회전했고 청소 되지 않은 빈칸
                    cnt += 1
                    q.append((nr,nc,i))
                    break
                # else:
                #     d -= 1
                #     if d<0:
                #         d += 4
        # 청소되지 않은 빈칸이 없는 경우
        if flag == 0:
            if d == 0:
                d = 2
                nr = r + dr[d]
                nc = c + dc[d]
                d = 0
            elif d==2:
                d=0
                nr = r + dr[d]
                nc = c + dc[d]
                d=2
            elif d==1:
                d = 3
                nr = r + dr[d]
                nc = c + dc[d]
                d=1
            elif d==3:
                d = 1
                nr = r + dr[d]
                nc = c + dc[d]
                d=3

            if 0<=nr<n and 0<=nc<m and board[nr][nc] != 1:
                q.append((nr,nc,d))
            elif 0<=nr<n and 0<=nc<m and board[nr][nc] == 1:
                return


n,m = map(int,input().split())

r,c,d = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

cnt = 1

b(r,c,d)
print(cnt)
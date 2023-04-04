'''
미세먼지를 제거하기 위해 공기청정기를 설치하려고 함
공기청정기의 성능을 테스트하기 위해 집을 R*C인 격자판으로 나타냄
각칸에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템 개발
공기청정기는 항상 1번 열에 설치되어 있음, 크기는 두 행을 차지
1초 동안 일어나는 일
    1. 미세먼지 확산됨 [모든 칸에서 동시에 일어난다.]
    - 네 방향으로 확산
    - 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않음
    - 확산되는 양 => Ar,c/5, 소수점은 버림
    2. 공기청정기 작동
    - 위쪽 공기청정기의 바람은 반시계방향으로 순환, 아래쪽 공기청정기의 바람은 시계방향으로 순환
    - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동함
    - 공기청정기에서 부는 바람은 미세먼지가 없는 바람,
    - 공기청정기로 들어간 미세먼지는 모두 정화됨
'''
# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

r, c, t = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(r)]

공청기 = []
for i in range(r):
    if board[i][0] == -1:
        공청기.append(i)

for tc in range(t):
    for i in range(r):
        for j in range(c):
            if board[i][j] != -1 and board[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nr = i+dr[k]
                    nc = j+dc[k]
                    if 0<=nr<r and 0<=nc<c and board[i][j] != -1:
                        board[nr][nc] += board[i][j]//5
                        cnt += 1
                board[i][j] = board[i][j]-(board[i][j]//5)*(cnt)
    print(공청기)
    # 공청기 위에
    r,c = 공청기[0],1
    d = 0
    dr = [0,-1,0,1]
    dc = [1,0,-1,0]
    before = 0
    while True:
        nr = r + dr[d]
        nc = c + dr[d]
        if r == 공청기[0] and c == 1:
            break
        if nr <0 or nr>=r or nc <0 or nc>=c:
            d += 1
            if d>=4:
                d = 0
            continue
        board[r][c], before = before,board[r][c]
        r = nr
        c = nc

    # 공청기 아래
    r, c = 공청기[1], 1
    d = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    before = 0
    while True:
        nr = r + dr[d]
        nc = c + dr[d]
        if r == 공청기[0] and c == 1:
            break
        if nr < 0 or nr >= r or nc < 0 or nc >= c:
            d += 1
            if d>=4:
                d = 0
            continue
        board[r][c], before = before, board[r][c]
        r = nr
        c = nc

    print(board)

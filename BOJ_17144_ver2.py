
# 4방향 탐색
dr = [-1,1,0,0]
dc = [0,0,-1,1]

r,c,t = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(r)]

# 현재 공청기 위치 알기
공청기위치=[]
for i in range(r):
    if board[i][0] == -1:
        공청기위치.append([i,0])

        
# 1. 미세먼지 확산
def 미세먼지():
    tmp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                flag = 0
                for k in range(4):
                    nr,nc = i+dr[k], j+dc[k]
                    if 0<=nr<r and 0<=nc<c and board[nr][nc] != -1:
                        tmp[nr][nc] += board[i][j]//5
                        flag += board[i][j] //5
                board[i][j] -= flag
    for i in range(r):
        for j in range(c):
            board[i][j] += tmp[i][j]

# 2. 공기청정기 위쪽

def 위쪽():
    dr = [0,-1,0,1]
    dc = [1,0,-1,0]
    d = 0
    before = 0
    x,y = 공청기위치[0][0], 1
    while True:
        nx = x+dr[d]
        ny = y+dc[d]
        if x == 공청기위치[0][0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue
        board[x][y], before = before,board[x][y]
        x = nx
        y = ny

# 3. 공기청정기 아래쪽
def 아래쪽():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    before = 0
    x, y = 공청기위치[1][0], 1
    while True:
        nx = x + dr[d]
        ny = y + dc[d]
        if x == 공청기위치[1][0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue
        board[x][y], before = before, board[x][y]
        x = nx
        y = ny

for _ in range(t):
    미세먼지()
    위쪽()
    아래쪽()

cnt = 0
for i in range(r):
    for j in range(c):
       if board[i][j] !=0 and board[i][j] != -1:
           cnt += board[i][j]
print(cnt)

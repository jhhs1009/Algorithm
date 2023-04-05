from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

아기상어 = 2

def 상어위치():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                상어위치r, 상어위치c = i,j
                return 상어위치r, 상어위치c

def bestfish(r,c,아기상어):
    vis = [[0]*N for _ in range(N)]
    dis = [[0]*N for _ in range(N)]

    q = deque()
    vis[r][c] = 1
    q.append((r,c))
    tmp = []
    while q:
        r,c= q.popleft()

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]

            if 0<=nr<N and 0<=nc<N and vis[nr][nc] == 0:
                if board[nr][nc]<=아기상어:
                    q.append((nr,nc))
                    dis[nr][nc] = dis[r][c] + 1
                    vis[nr][nc] = 1
                    if board[nr][nc]<아기상어 and board[nr][nc] != 0:
                        tmp.append((nr,nc,dis[nr][nc]))
    return sorted(tmp, key=lambda x:(-x[2], -x[0], -x[1]))
result = 0
cnt = 0
r, c = 상어위치()
while True:
    a = bestfish(r, c,아기상어)

    if len(a) == 0:
        break

    nx, ny, dist = a.pop()
    result += dist
    board[r][c], board[nx][ny] = 0,0
    r, c = nx,ny
    cnt += 1
    if cnt == 아기상어:
        아기상어 += 1
        cnt = 0

print(result)
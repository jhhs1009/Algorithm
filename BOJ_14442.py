from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def b(r,c):
    q = deque()
    q.append((r,c,k))
    vis = [[[0]*(k+1) for _ in range(M)] for _ in range(N)]
    vis[r][c][k] = 1
    while q:
        r,c,result = q.popleft()

        if r==N-1 and c==M-1:
            return vis[N-1][M-1][result]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and map[nr][nc] == 0 and vis[nr][nc][result]==0:
                vis[nr][nc][result] = vis[r][c][result] + 1
                q.append((nr, nc, result))

            elif 0<=nr<N and 0<=nc<M and map[nr][nc]== 1 and result>0 and vis[nr][nc][result-1]==0:
                vis[nr][nc][result-1] = vis[r][c][result] + 1
                q.append((nr, nc, result-1))

    return -1


N, M, k = map(int,input().split())

map = [list(map(int,input())) for _ in range(N)]


print(b(0,0))
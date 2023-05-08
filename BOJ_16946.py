
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def b(r,c):
    q = deque()
    q.append((r,c,0))
    vis = [[[0] for _ in range(M)] for _ in range(N)]
    vis[r][c][0] = 1
    while q:
        r,c,result = q.popleft()

        if r==N-1 and c==M-1:
            return vis

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M:
                if map[nr][nc] != 0:
                    vis[nr][nc]
                    q.append((nr,nc,))



N, M = map(int,input().split())

map = [list(map(int,input())) for _ in range(N)]


print(b(0,0))

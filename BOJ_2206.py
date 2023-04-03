'''
벽 부수고 이동하기

M*M 행렬로 표현되는 맵이 있다.

맵에서 0은 이동할 수 있는 곳을 나타내고
1은 이동할 수 없는 벽이 있는 곳을 나타낸다.

0 : 길
1 : 벽

(1,1)에서 (N,M)의 위치까지 이동하려 하는데, 최단 경로로 이동하려고 한다.

최단 경로 = 맵에서 가장 적은 개수의 칸을 지나는 경로를 말함
시작하는 칸과 끝나는 칸도 포함해서 센다.


이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

3차원 배열로 생각을 해서 vis에 방문 여부와 함께 벽을 깼는지의 여부를 넣기
'''
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def b(r,c):
    q = deque()
    q.append((r,c,0))
    vis = [[[0]*2 for _ in range(M)] for _ in range(N)]
    vis[r][c][0] = 1
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

            elif 0<=nr<N and 0<=nc<M and map[nr][nc]== 1 and result==0:
                vis[nr][nc][1] = vis[r][c][0] + 1
                q.append((nr, nc, 1))

    return -1


N, M = map(int,input().split())

map = [list(map(int,input())) for _ in range(N)]


print(b(0,0))

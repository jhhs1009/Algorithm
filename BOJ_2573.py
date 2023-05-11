from collections import deque
from copy import deepcopy

dr = [-1,1,0,0]
dc = [0,0,-1,1]

n,m = map(int,input().split())

num_list = [list(map(int,input().split())) for _ in range(n)]

'''
전체적으로 한 번 돌 때

1. 4방향 탐색 -> 0인거 카운트 해주기
2. 현재 값의 방문 배열에 표시하기 vis
'''
def b(r,c,tmp):
    cnt = 0

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<n and 0<=nc<m and num_list[nr][nc]==0:
            cnt += 1
    if num_list[r][c]-cnt>=0:
        tmp[r][c] -= cnt
    else:
        tmp[r][c] = 0

    return tmp

def bfs(ice):
    r, c = ice.popleft()
    q =deque()
    q.append((r,c))
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and tmp[nr][nc]!=0 and vis[nr][nc]==1:
                q.append((nr,nc))
                vis[nr][nc] = 0


tmp = deepcopy(num_list)
# 먼저 판단을 해야 함 이게 이상한건지 아닌지
ice = deque()
vis = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if num_list[i][j] !=0:
            # 감소 전에 해야할 일이 존재
            ice.append((i,j))
            vis[i][j] = 1
cnt = 0
while ice:
    cnt += bfs(ice)



for i in range(n):
    for j in range(m):
        if num_list[i][j] !=0:
            # 감소 해야 함
            tmp = b(i,j,tmp)
# 감소 후 결과가 tmp

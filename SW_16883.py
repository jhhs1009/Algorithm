'''
n*n 칸에 숫자가 적힌 판이 주어짐
오른쪽이나 아래로만 이동 가능

맨 왼쪽 위에서(0,0) 오른쪽 아래 까지 이동할 때, 숫자의 합계가 최소가 되도록 움직이면
이때의 합이 얼마인지 출력해라

0,0 -> n-1,n-1

'''
from collections import deque

def dfs(r,c):
    dr = [0,1]
    dc = [1,0,]

    vis = [[0]*(n) for _  in range(n)]
    q = deque()
    q.append((r,c))
    vis[r][c] = num_list[r][c]

    while q:
        r,c = q.popleft()

        if r==n-1 and c==n-1:
            return vis

        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<n:
                plus = vis[r][c]+num_list[nr][nc]
                if vis[nr][nc] !=0 and plus<vis[nr][nc]:
                    vis[nr][nc] = plus
                elif vis[nr][nc] == 0:
                    vis[nr][nc] = plus
                q.append((nr,nc))




T = int(input())
for i in range(T):
    n = int(input())
    num_list = [list(map(int,input().split())) for _ in range(n)]

    vis = (dfs(0,0))
    print(f"#{i+1} {vis[n-1][n-1]}")


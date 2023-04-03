'''
체스판 위에 한 나이트가 놓여져 있다.
나이트가 한 번에 이동할 수 있는 칸은 그림과 같다.
나이트가 이동하려고 하는 칸이 주어진다.
몇 번 움직이면 이 칸으로 이동할 수 있음?

'''
dr = [-2,-1,1,2,2,1,-1,-2]
dc = [1,2,2,1,-1,-2,-2,-1]


def d(r,c):
    q = []
    q.append((r,c))
    vis = [[1]*l for _ in range(l)]
    while q:
        r,c = q.pop(0)
        if r == rr and c==cc:
            return vis

        for i in range(8):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<l and 0<=nc<l and vis[nr][nc] == 1:
                q.append((nr,nc))
                vis[nr][nc] += vis[r][c]



T = int(input())

for tc in range(T):
    l = int(input())

    r,c = map(int,input().split())
    rr, cc = map(int,input().split())

    vis = d(r,c)
    print(vis[rr][cc]-1)
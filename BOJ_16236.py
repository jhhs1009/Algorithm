'''
아기 상어
처음의 아기상어 크기 = 2
상하좌우로 인접한 한 칸씩 이동

처음에 아기 상어의 크기 = 2

'''
from collections import deque

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def 위치():
    상어위치 = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                상어위치.append([i, j])
                return  상어위치

def bfs(r,c):
    global s, cnt, res
    q = deque()
    q.append((r,c,0))
    vis = [[0]*n for _ in range(n)]
    vis[r][c] = 1

    while q:
        r,c,cnt = q.popleft()

        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]

            if 0<=nr<n and 0<=nc<n and vis[nr][nc] == 0:
                vis[nr][nc] = 1
                b = sum(board,[])
                if b.count(0) == n*n-1:
                    return
                else:
                    cnt += 1
                    q.append((nr, nc, cnt))
                    cnt -= 1
                    if board[nr][nc] != 0:
                        if board[nr][nc] < s:
                            s +=1
                            board[nr][nc] = 0
                            res += cnt
                        elif board[nr][nc] == s:
                            board[nr][nc] = 0
                        else:
                            board[nr][nc] = 0

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

상어위치 = 위치()

s = 2
cnt = 0
res = 0
bfs(상어위치[0][0], 상어위치[0][1])
print(res)

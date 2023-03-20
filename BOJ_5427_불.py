'''
상근이는 출구를 향해 뛰고 있다.
매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다.
벽에는 불이 붙지 않는다.
벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 ㅇ벗다.
빨리 탈출

. : 빈공간
# : 벽
@ : 상근이의 시작 위치
* : 불

w = 열
h = 행

풀이
- 외곽으로 나가기만 하면 끝인데 외곽으로 나가는 번호는 끝 인덱스
'''
from collections import deque

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def check():
    for i in range(h):
        for j in range(w):
            if board[i][j] == "@":
                return i,j

def check_f():
    불 = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == "*":
                불.append([i,j])
    return 불

def f(불):
    for i in range(len(불)):
        r = 불[i][0]
        c = 불[i][1]
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0<=nr<h and 0<=nc<w and board[nr][nc] != "#":
                board[nr][nc] = "*"
    return board


def bfs(r,c,board):
    vis = [[1]*w for _ in range(h)]
    q = deque()
    q.append((r,c))
    res = 0
    while q:
        r,c = q.popleft()
        cnt = 0
        if len(q)==1:
            불 = check_f()
            board = f(불)
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<h and 0<=nc<w and vis[nr][nc] == 1 and board[nr][nc]==".":
                vis[nr][nc] += vis[r][c]
                q.append((nr,nc))
                cnt += 1
                if nr == 0 or nc == 0 or nr ==h-1 or nc == w-1:
                    vis = sum(vis,[])
                    return print(max(vis))
                if board[r][c] != "*":
                    board[r][c] = "."
                board[nr][nc] = "@"
                res += cnt

    else:
        return print('IMPOSSIBLE')



t = int(input())

for tc in range(t):
    w,h = map(int,input().split())
    board = [list(map(str,input())) for _ in range(h)]

    r,c = check()
    불 = check_f()
    board = f(불)
    bfs(r,c,board)
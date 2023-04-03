'''
적록색약

빨간색과 초록색의 차이를 거의 느끼지 못함

적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 조금 다름

크기가 N*N인 그리드의 각 칸에 R,G,B

구역은 같은 색으로 이루어져 있다.
같은 색상이 상하좌우로 인접해 있는 경우에 두글자는 같은 구역에 속함

적록색약 -> 빨간색과 초록색의 차이를 느낄 수 없음
'''
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def b(r,c, color,board):
    q = []
    q.append((r,c))
    vis[r][c] = 1

    while q:
        r,c = q.pop(0)

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<T and 0<=nc<T and vis[nr][nc]==0:
                if board[nr][nc] == color:
                    q.append((nr,nc))
                    vis[nr][nc] = 1


T = int(input())

board = [list(map(str,input())) for _ in range(T)]
non = [[0]*T for _ in range(T)]
vis = [[0]*T for _ in range(T)]

for i in range(T):
    for j in range(T):
        if board[i][j] == "R":
            non[i][j] = "G"
        else:
            non[i][j] = board[i][j]

cnt = 0
for i in range(T):
    for j in range(T):
        if vis[i][j] ==0:
            b(i,j,board[i][j],board)
            cnt += 1

vis = [[0]*T for _ in range(T)]
cnt_non = 0
for i in range(T):
    for j in range(T):
        if vis[i][j] == 0:
            b(i,j,non[i][j],non)
            cnt_non += 1

print(cnt)
print(cnt_non)



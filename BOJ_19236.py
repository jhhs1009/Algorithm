'''
청소년 상어

물고기는 번호와 방향을 가짐
번호 : 1~16사이
방향 : 8개

* 규칙
- 번호가 작은 물고기부터 순서대로 이동함
- 한 칸을 이동할 수 있고,
- 이동할 수 있는 칸
    = 빈 칸
    = 다른 물고기가 있는 칸
- 이동할 수 없는 칸
    = 상어가 존재
    = 공간의 경계를 넘는 칸
- 물고기 이동이 끝나면 상어 이동
- 한 번에 여러 개의 칸 이동 가능
- 물고기가 있는 칸으로 이동했다면, 그 칸의 물고기 먹고, 물고기의 방향 가짐
- 이동할 수 있는 칸이 없으면 집으로 감감
'''
from collections import deque

# 방향 순서
dr = [-1,-1,0,1,1,1,0,-1] # 행
dc = [0,-1,-1,-1,0,1,1,1] # 열

def 물고기위치(k):
    global 물고기
    for k in range(1,17):
        for i in range(4):
            for j in range(4):
                if board_cus[i][j][0] == k:
                    물고기.append([i, j])

def fish_move(r,c,dir):
    # board_cus의 행, 열 값 + 방향 가중치 까지 가지고 옴
    # 상어 아니고 이동할 수 있을 때까지 dir 값 1씩 증가하고 위치 바꾸고
    # board_cus를 통채로 바꾸기
    for i in range(8):
        nr = r+dr[dir-1]
        nc = c+dc[dir-1]
        if 0<=nr<4 and 0<=nc<4 and board_cus[nr][nc][0]!="상":
            board_cus[r][c], board_cus[nr][nc] = board_cus[nr][nc], board_cus[r][c]
            return board_cus
        else:
            dir += 1
            if dir == 9:
                dir = 1
            board_cus[r][c][1] = dir


def shark_move(r,c,dir,res):
    # 상어가 바깥으로 나가게 되면 끝남

    nr = r+dr[dir-1]
    nc = c+dc[dir-1]
    print(board_cus[nr][nc])
    if 0<=nr<4 and 0<=nc<4:
        res +=board_cus[nr][nc][0]
        board_cus[r][c], board_cus[nr][nc] = [0,0], board_cus[r][c]
        return board_cus, res



# 시작
board = [list(map(int,input().split())) for _ in range(4)]

# input값 커스텀
board_cus = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(0, 8, 2):
        board_cus[i][j//2] = board[i][j:j+2]

cnt = 0
# 2. 물고기 1번부터 16번까지 계속 돈다. 지금 현재 위치가 상어가 아니라면
for i in range(15-cnt):
    if i == 0:
        # 1. 물고기 이동
        # 8개 방향 돌려서 0,0이 아니고 숫자 증가하는데
        물고기 = []
        물고기위치(1)

        # 1-2) 처음 상어위치 고정
        board_cus[0][0][0] = "상"

    if board_cus[물고기[i][0]][물고기[i][1]][0] != "상":
        fish_move(물고기[i][0], 물고기[i][1], board_cus[물고기[i][0]][물고기[i][1]][1])
        if i == 14:
            break
        물고기=[]
        물고기위치(1)

print(f"물고기 이동 결과값: {board_cus}")


# 3. 상어 이동 해야 함.
상어r, 상어c = 0,0
dir =  board_cus[상어r][상어c][1]
res = 0

def a(상어r, 상어c):
    q = deque()
    q.append((상어r,상어c))

    global dir
    global res

    visi = [[0]*4 for _ in range(4)]

    visi[상어r][상어c] = 1
    while q:
        상어r,상어c = q.popleft()

        while True:
            nr, nc = 상어r+dr[dir-1], 상어c+dc[dir-1]
            board_cus,res = shark_move(상어r, 상어c, dir,res)

a(상어r, 상어c)
from collections import deque

# 방향 순서
dr = [-1,-1,0,1,1,1,0,-1] # 행
dc = [0,-1,-1,-1,0,1,1,1] # 열

def 물고기위치(k):
    물고기 = []
    for k in range(1,17):
        for i in range(4):
            for j in range(4):
                if board_cus[i][j][0] == k:
                    물고기.append([i, j])
    return 물고기

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

def 물고기순서(cnt, 물고기):
    for i in range(15 - cnt):

        if board_cus[물고기[i][0]][물고기[i][1]][0] != "상":
            fish_move(물고기[i][0], 물고기[i][1], board_cus[물고기[i][0]][물고기[i][1]][1])
            if i == 14:
                break
            물고기 = []
            물고기위치(1)
    return board_cus

# 시작 위치
board = [list(map(int,input().split())) for _ in range(4)]

# input값 커스텀
board_cus = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(0, 8, 2):
        board_cus[i][j//2] = board[i][j:j+2]

def dfs(r,c,res,board_cus, cnt):
    # 1.물고기 이동
    # - 물고기 순서를 찾고
    물고기 = 물고기위치(1)
    board_cus[0][0][0] = "상"

    # - 물고기가 움직여야 함
    board_cus = 물고기순서(cnt,물고기)
    print(f"물고기 이동 결과값: {board_cus}")


dfs(0,0,0,board_cus,0)


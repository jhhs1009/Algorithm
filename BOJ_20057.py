'''
마법사 상어와 토네이도

토네이도를 크기가 N*N인 격자로 나누어진 모래밭에서 연습하려고 함

위치(r,c) -> 격자의 r행 c열을 의미
A[r][c]는 (r,c)에 있는 모래의 양을 의미함

토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작됨
한 번에 한 칸 이동

y의 모든 모래가 비율과 a가 적혀있는 칸으로 이동
비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율 만큼
소수점 아래는 버림

a로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같음

모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다.

구현, 시뮬레이션 문제
'''

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

# 밖으로 나간 모래양
answer = 0
# 현재 x좌표, y좌표
now = [N//2, N//2]

# 왼쪽으로 퍼질 때
left = [(-2,0,0.02), (2,0,0.02), (-1,-1,0.1), (-1,0,0.07),
        (-1,1,0.01), (1,-1,0.1), (1,0,0.07),(1,1,0.01), (0,-2,0.05), (0,-1,0)]
# 오른쪽으로 퍼질 때
right = [(x,-y,z) for x,y,z in left]
# 아래쪽으로 퍼질 때
down = [(-y, x, z) for x,y,z in left]
# 위쪽으로 퍼질 때
up = [(-x, y, z) for x,y,z in down]

rate = {"left":left, "right":right, "down":down, "up":up}

def move(cnt, dx, dy, dir):
    global answer
    for _ in range(cnt+1):
        # 현재좌표 업데이트
        now[0], now[1] = now[0]+dx, now[1]+dy
        # 회오리를 돌다가 끝나버린 경우
        if now[0] < 0 or now[1] < 0:
            break

        # 모래가 퍼진 값을 누적한 양
        spreads = 0
        # 퍼지는 모래 계산
        for dx, dy, r in rate[dir]:
            nx = now[0] + dx
            ny = now[1] + dy
            # 퍼지지 않는 모래들은 현재 자리에 누적해주기
            if r == 0:
                sand = board[now[0]][now[1]] - spreads
            else:
                sand = int(board[now[0]][now[1]]*r)
            # 모래 양 업데이트
            if 0<=nx<N and 0<=ny<N:
                board[nx][ny] += sand
            else:  # 범위 밖 : 정답 누적값 업데이트
                answer += sand
            spreads += sand    # 현재자리 계산을 위한 퍼지는 모래의 누적값

for i in range(N):
    if i % 2 == 0:
        move(i, 0, -1, 'left')
        move(i, 1, 0, 'down')
    else:
        move(i, 0, 1, 'right')
        move(i, -1, 0, 'up')

print(answer)
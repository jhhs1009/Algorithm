from collections import deque

# 4방향 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global dq, fire
    
    # dq = 사람이 이동할 위치, 이동할 곳이 없어 비었다면 반복 종료
    # 사람이 있는 큐
    while dq:
        temp = deque()  # 임시 deque생성 = dq를 현재 dq에 저장된 길이만큼만 반복하기 위해서
        while dq:
            r, c = dq.popleft()
            # r이나 c가 빌딩 끝(출구)에 도착했고, 그 칸이 불이 아니라면
            if (r == 0 or c == 0 or r == m - 1 or c == n - 1) and building[r][c] != '*':
                # 현재 칸에 저장된 수를 리턴
                return building[r][c]
            for d in range(4):  # 4방향 탐색
                nr, nc = r + dr[d], c + dc[d]
                # nr, nc가 유효한 범위이고, 이동할 칸이 '.'(불, 벽아님), 현재 칸이 불이아니라면
                if 0 <= nr < m and 0 <= nc < n and building[nr][nc] == '.' and building[r][c] != '*':
                    # 이동할 칸에 현재칸 +1값 저장하고 임시데큐에 저장
                    building[nr][nc] = building[r][c] + 1
                    temp.append((nr, nc))
        # 다시 반복할때 temp에 저장된 요소를 반복하도록 dq에 temp저장하고 초기화
        dq = temp
        temp = deque()
        while fire:
            r, c = fire.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                # 4방향 탐색, 이동할 칸이 유효범위이고 벽이아니라면
                if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] == 0 and building[nr][nc] != '#':
                    # 이동할 칸을 불이났다고 표시
                    building[nr][nc] = "*"
                    visited[nr][nc] = 1  # 방문처리
                    temp.append((nr, nc))  # 임시데큐에 저장
        fire = temp  # fire deque에 임시deque값 저장
        
T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    building = [list(input()) for _ in range(m)]
    visited = [[0] * n for _ in range(m)]

# dq = 사람이 움직일 위치, fire = 불이 이동하는 위치
dq, fire = deque(), deque()
for i in range(m):
    for j in range(n):
        # 빌딩에서 불이 난 곳은 visited 1로 체크하고 fire에 추가
        if building[i][j] == '*':
            visited[i][j] = 1
            fire.append((i, j))
        # 빌딩에 사람이 있는 곳은 @를 0으로 바꿔 표시하고 dq에 추가
        elif building[i][j] == '@':
            building[i][j] = 0
            dq.append((i, j))

rlt = bfs()
# 리턴값이 있다면 리턴값+1 출력(건물끝에서 건물밖으로 나가는시간 +1), 리턴이 없다면 "IMPOSSIBLE" 출력
print(rlt + 1 if rlt != None else "IMPOSSIBLE")
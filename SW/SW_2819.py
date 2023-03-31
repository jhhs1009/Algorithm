'''
동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동
각 칸에 적혀 있는 숫자를 차례대로 이어 붙이면 7자리의 숫자가 됨

다시 방문 가능

0으로 시작하는 수를 만들 수도 있음

서로 다른 일곱 자리 수들의 개수?

'''
# 상 하 좌 우
dr = [-1,1,0,0] # 행
dc = [0,0,-1,1] # 열

def b(r,c,res):

    res += str(board[r][c])

    if len(res) == 7:
        s.add(res)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<4 and 0<=nc<4:
            b(nr,nc,res)


T = int(input())

for tc in range(T):
    board = [list(map(int,input().split())) for _ in range(4)]
    cnt = 0
    r = 0
    res = ""
    s = set()
    for i in range(4):
        for j in range(4):
            b(i,j,res)
    print(f"#{tc+1} {len(s)}")

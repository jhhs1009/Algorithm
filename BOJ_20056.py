'''
마법사 상어와 파이어볼

N*N 격자에 파이어볼 M개를 발사

처음 파이어볼 : 각자 위치에서 이동 대기

격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고,
1번 열은 N번 열과 연결되어 있음

파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 아래와 같다.
7 0 1
6   2
5 4 3

마법사 상어가 모든 파이어볼에게 이동을 명령하면 아래와 같은 일이 일어남
1. 모든 파이어볼이 자신의 방향 d로 속력 s만큼 이동
    - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
2. 이동이 끝난 뒤 2개 이상의 파이어볼이 있는 칸
    i. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐짐
    ii. 파이어볼은 4개의 파이어볼로 나눠짐
    iii. 나누어진 파이어볼의 질량, 속력, 방향은 아래와 같다.
        a. 질량 = 합쳐진 파이어볼 질량의 합 /5
        b. 속력 = 합쳐진 파이어볼 속력의 합 / 합쳐진 파이어볼의 개수
        c. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면,
            방향은 0,2,4,6이 되고, 
            섞여 있으면 1,3,5,7이 됨
    iv. 질량이 0인 파이어볼은 소멸되어 없어짐

이동을 k번 명령한 후, 남아있는 파이어볼 질량의 합은?

'''
from collections import deque

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

n,m,k = map(int,input().split())

filed = [[[0]*3 for _ in range(n)] for _ in range(n)]

ball = []
for i in range(m):
    r,c,kg,s,d = map(int,input().split())

    filed[r-1][c-1] = [kg,s,d]
    ball.append([r-1,c-1])
# for i in range(n):
#     print(filed[i])
# print("========================================")

def move(filed,ball):
    # 1. 모든 파이어볼이 자신의 방향 d로 속력 s만큼 이동
    # vis 만들어서 판단
    vis = [[0]*n for _ in range(n)]
    # 인덱스 넣기
    q = []
    new_ball = []
    for i in range(m):
        r,c = ball[i][0], ball[i][1]
        print(r,c)

        nr = r + dr[filed[r][c][2]]*filed[r][c][1]
        nc = c + dc[filed[r][c][2]]*filed[r][c][1]

        if 0<=nr<n and 0<=nc<n:
            if filed[nr][nc] == [0,0,0]:
                filed[nr][nc] = filed[r][c]
            else:
                tmp = filed[nr][nc]
                임시 = []
                임시.append(tmp)
                임시.append(filed[r][c])
                filed[nr][nc] = 임시
            filed[r][c] = [0, 0, 0]
            vis[nr][nc] += 1
            if [nr,nc] not in new_ball:
                new_ball.append([nr,nc])
            if vis[nr][nc] == 2:
                q.append([nr,nc])
    # 여기 위에 까지가 이제 이동 끝

    # 2. 2개 이상의 파이어볼 판단
    # q에 들어있는 인덱스 값은 무조건 파이어볼이 2개 이상인 것

    for idx in q:
        a = [0,0,0]
        flag_짝 = 0
        flag_홀 = 0
        for i in range(len(filed[idx[0]][idx[1]])):
            # zip 함수를 이용해 두 리스트 값 더하기
            # 방향 탐색 flag
            if filed[idx[0]][idx[1]][i][2] % 2 == 0:
                flag_짝 += 1
            elif filed[idx[0]][idx[1]][i][2] % 2 == 1:
                flag_홀 += 1

            c = [x+y for x,y in zip(a,filed[idx[0]][idx[1]][i])]
            a = c
        # print(vis[idx[0]][idx[1]])
        # print(a)
        질량 = a[0]//5
        속력 = a[1]//vis[idx[0]][idx[1]]
        if flag_홀 == vis[idx[0]][idx[1]] or flag_짝 == vis[idx[0]][idx[1]]:
            방향 = [0,2,4,6]
        else:
            방향 = [1,3,5,7]
        임시 = []
        for k in range(4):
            a = []
            a.append(질량)
            a.append(속력)
            a.append(방향[k])
            임시.append(a)
        filed[idx[0]][idx[1]] = 임시
    return filed, new_ball

for i in range(k):
    temp, new_ball = move(filed, ball)
    filed = temp
    ball = new_ball
res = 0
for i in range(n):
    for j in range(n):
        if filed[i][j] != [0,0,0]:
            for w in range(len(filed[i][j])):
                res += filed[i][j][w][0]

print(res)

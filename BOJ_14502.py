'''
N*M 직사각형으로 나타낼 수 있다.

바이러스는 상하좌우로 인접한 빈 칸으로 퍼져나갈 수 있다.

새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

0 : 빈 칸
1 : 벽
2 : 바이러스가 있는 곳

'''
from collections import deque
# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 조합 만들기
def b(i,arr):
    global res
    if len(arr) == 3:
        res.append(arr)
        return

    for j in range(i,len(idx)):
        b(j+1, arr+[idx_num[j]])

# 벽을 안세운 새로운 보드 만들기
def n_():
    new_ = [[0] * m for _ in range(n)]
    for j in range(n):
        for k in range(m):
            new_[j][k] = board[j][k]
    return new_

def bfs(r,c):
    q = deque()
    q.append((r,c))

    while q:
        r,c = q.popleft()
        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]
            if 0<=nr<n and 0<=nc<m and new_[nr][nc] == 0:
                new_[nr][nc] = 2
                q.append((nr,nc))
    return new_


n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

idx = []
q_idx = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            idx.append([i,j])
        elif board[i][j] == 2:
            q_idx.append([i,j])

idx_num = [x for x in range(len(idx))]
res = []
# 조합해서 뽑아옴
b(0,[])

new_ = n_()


result = 0
for i in range(len(res)):
    for j in range(len(res[i])):
        # 벽세우기
        new_[idx[res[i][j]][0]][idx[res[i][j]][1]] = 1
    # BFS를 돌려야지
    # new_ 를 돌려야지
    # 벽 세워져 있음
    for k in range(len(q_idx)):
        new_ = bfs(q_idx[k][0],q_idx[k][1])
    # 바이러스, 벽 완료
    # 안전구역 찾기
    cnt = 0
    for k in range(n):
        cnt += new_[k].count(0)
    if cnt>result:
        result = cnt
    new_ = n_()
print(result)


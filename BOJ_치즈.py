from collections import deque

def bfs():
    q = deque([(0, 0)])
    delete = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny]:
                vis[nx][ny] = 1
                if c[nx][ny] == 0:  
                    q.append((nx, ny))
                elif c[nx][ny] == 1:  
                    delete.append((nx, ny))
                    
    for x, y in delete:
        c[x][y] = 0  
    return len(delete)  

n, m = map(int, input().split())
c = []
cnt = 0
for i in range(n):
    c.append(list(map(int, input().split())))
    cnt += sum(c[i])  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    vis = [[0] * m for _ in range(n)]
    deleteCnt = bfs()
    cnt -= deleteCnt
    if cnt == 0:  
        print(time, deleteCnt, sep='\n') 
        break
    time += 1
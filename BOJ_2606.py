'''
바이러스

신종 바이러스

'''

def dfs(number):
    global cnt
    vis[number] = 1
    for i in board[number]:
        if vis[i] ==0:
            dfs(i)
            cnt += 1

n = int(input())
m = int(input())
num_list = [list(map(int,input().split())) for _ in range(m)]

board = [[]*n for i in range(n+1)]
vis = [0]*(n+1)

for i in range(m):
    board[num_list[i][0]].append(num_list[i][1])
    board[num_list[i][1]].append(num_list[i][0])

cnt = 0
dfs(1)
print(cnt)
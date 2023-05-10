'''
빙산

0의 갯수 만큼 줄어듬

'''
from copy import deepcopy

dr = [-1,1,0,0] #행
dc = [0,0,-1,1] #열

def bb(r,c):
    cnt = 0
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<n and 0<=nc<m and num_list[nr][nc]==0 and num_list[r][c]>0:
            cnt+=1
    return cnt


def f():
    zero = 0
    array = deepcopy(num_list)
    for i in range(n):
        for j in range(m):
            if num_list[i][j] != 0:
                cnt = bb(i, j)
                if cnt == 4:
                    return 1
                if array[i][j]-cnt>=0:
                    tmp[i][j] = array[i][j]-cnt
    return -1


n,m = map(int,input().split())
num_list = [list(map(int,input().split())) for _ in range(n)]

count = 0
flag = 0
while True:
    tmp = [[0] * m for _ in range(n)]
    print(tmp)

    if flag == 1 or flag == -1:
        print(flag)
        break
    flag = f()
    count += 1

print(tmp)

if flag == 1:
    print(count)
else:
    print(0)
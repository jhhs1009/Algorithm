'''
처음의 아기상어 크기 = 2
상하좌우로 인접한 한 칸씩 이동

처음에 아기 상어의 크기 = 2

'''
def 위치():
    상어위치 = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                상어위치.append([i, j])
                return  상어위치

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

상어위치 = 위치()

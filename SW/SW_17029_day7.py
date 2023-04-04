T = int(input())

for tc in range(T):
    n = int(input())

    board = [list(map(int,input().split())) for _ in range(n)]

    print(board)
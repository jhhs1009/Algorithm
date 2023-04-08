'''
1부터 N까지 자연수 중에서 M개를 고른 수열, 중복되는 수열 여러 번 출력 안됨
'''

n,m = map(int,input().split())

arr = sorted(list(map(int,input().split())))
vis = [False]* n
lst = []


def dfs():
    if len(lst) == m:
        print(*lst)
        return
    remember = 0
    for i in range(n):
        if not vis[i] and remember != arr[i]:
            vis[i] = True
            lst.append(arr[i])
            remember = arr[i]
            dfs()
            vis[i] = False
            lst.pop()

dfs()

'''
1부터 N까지 자연수 중에서 M개를 고른 수열이 오름차순이어야 함
'''

n,m = map(int,input().split())

arr = list(map(int,input().split()))

arr = sorted(arr)

lst = []

def dfs(x):
    if len(lst) == m:
        print(' '.join(map(str,lst)))
        return
    for i in range(x,n):
        if arr[i] not in lst:
            lst.append(arr[i])
            dfs(i+1)
            lst.pop()

dfs(0)
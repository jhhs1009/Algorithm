'''
1부터 N까지 자연수 중에서 M개를 고른 수열, 중복 허용, 비내림차순? 오름 차순인가
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
        lst.append(arr[i])
        dfs(i)
        lst.pop()

dfs(0)
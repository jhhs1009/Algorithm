n,m = map(int,input().split())

arr = sorted(list(map(int,input().split())))
vis = [False]* n
lst = []

def dfs(x):
    if len(lst) == m:
        print(*lst)
        return
    remember = 0
    
    for i in range(x,n):
        if  remember != arr[i]:
            lst.append(arr[i])
            vis[i] = True
            dfs(i)
            vis[i] = False
            remember = arr[i]
            lst.pop()     
dfs(0)
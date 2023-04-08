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
        if remember != arr[i]:
            lst.append(arr[i])
            vis[i] = True
            dfs()
            vis[i] = False
            remember = arr[i]
            lst.pop()     
dfs()
        
    
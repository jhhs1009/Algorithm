n,m = map(int,input().split())

arr = list(map(int,input().split()))

arr = sorted(arr)

lst = []
def dfs():
    if len(lst)==m:
        print(' '.join(map(str,lst)))
        return
    
    for i in range(0,n):
        if arr[i] not in lst:
            lst.append(arr[i])
            dfs()
            lst.pop()

dfs()

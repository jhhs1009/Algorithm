'''
수빈이는 현재 점 N에 있고, 동생은 점 k에 있다.
수빈이는 걷거나 순간이동을 할 수 있다.
수빈이의 위치가 X일 때 걷는다면 1초 후에 x-1 x+1로 이동하게 됨
순간이동을 하는 경우에는 1초 후에 2*x의 위치로 이동하게 됨

수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하라
'''
def dfs(n,cnt):
    if n==k:
        return cnt
    if 0<=n:
        dfs(n-1, cnt+1)
        dfs(n+1, cnt+1)
        dfs(n*2, cnt+1)
    else:
        return


n,k = map(int,input().split())
dfs(n,0)

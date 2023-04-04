'''
걸리는 최소한의 거리가 얼마인지 출력하는 프로그램을 만드시오

0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마지?
'''
def dijkstra(s, V):
    U = [0] * (V + 1)
    U[s] = 1
    D[s] = 0

    for e, w in adjl[s]:
        D[e] = w

    for _ in range(V):

        minV = INF
        t = 0

        for i in range(V + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i

        U[t] = 1

        for e, w in adjl[t]:
            D[e] = min(D[e], D[t] + w)


T = int(input())

for tc in range(T):

    INF = 1000

    n,e = map(int,input().split())
    adjl = [[] for _ in range(n + 1)]

    for _ in range(e):
        s, e, w = map(int, input().split())
        adjl[s].append([e, w])

    D = [INF] *(n+1)

    dijkstra(0,n)
    print(f"#{tc+1} {D[n]}")

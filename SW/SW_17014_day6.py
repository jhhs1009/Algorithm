'''
6일차 응용 - 연산

자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오

연산의 중간 결과도 항상 백만 이하의 자연수여야 함

N = 2, M = 7인 경우 (2+1) * 2 + 1 = 7 이므로 최소 3번의 연산이 필요

흠 런타임 에러
'''
from collections import deque

def b(n,cnt):
    global vis
    q = deque()
    q.append((n,cnt))
    vis[n] = 1
    while q:
        num,cnt = q.popleft()
        if num == m:
            return cnt


        number = num + 1
        if 0<number <= 1000000 and vis[number] ==0:
            vis[number] = 1
            q.append((number, cnt+1))

        number = num - 1
        if 0<number <= 1000000 and vis[number] ==0:
            vis[number] = 1
            q.append((number, cnt+1))

        number = num * 2
        if 0<number <= 1000000 and vis[number] ==0:
            vis[number] = 1
            q.append((number, cnt+1))

        number = num -10
        if 0<number <= 1000000 and vis[number] ==0:
            vis[number] = 1
            q.append((number, cnt+1))


T = int(input())

for tc in range(T):
    n,m = map(int,input().split())

    vis = [0] * 1000001
    cnt = b(n,0)

    print(f"#{tc+1} {cnt}")


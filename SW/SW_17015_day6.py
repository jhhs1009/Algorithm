'''
6일차 응용 - 그룹 나누기

한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모든 같은 조가 된다.

번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

1부터 N까지의 출석번호가 있고
M장의 신청서가 제출되었을 때
전체 몇 개의 조가 만들어지는지 출력하는 프로그램을 만드시오

한 쌍으로 만들어야 함

내가 어떤 사람을 지목했을 때 그 사람이 조에 들어가 있다면
그 조에 포함된다
-> union find

부모를 저장하는 배열을 만든 뒤에 조가 만들어질 때 작은 번호를 가진 쪽으로 부모를 병합하는 과정으로
문제를 품

부모를 찾을 때는 재귀를 이용하여 찾음

서로소 집합 자료 구조
'''

def findSet(x):
    if p[x] == x:
        return x
    else:
        return findSet(p[x])

def union(x, y):
    p[findSet(y)] = findSet(x)

T = int(input())

for tc in range(T):
    n,m = map(int, input().split())
    m_list = list(map(int, input().split()))

    p = [0] * (n+1)

    for i in range(n+1):
        p[i] = i

    for i in range(m):
        union(m_list[i*2], m_list[i*2+1])

    root =[]
    for i in range(1,n+1):
        root.append(findSet(i))

    print(f"#{tc+1} {len(set(root))}")



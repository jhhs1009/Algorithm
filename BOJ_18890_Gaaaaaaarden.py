'''
시뮬레이션 어려운 문제

초록색 배양액과 빨간색 배양약을 땅에 적절하게 뿌려서 꽃을 피울 것
배양액을 뿌릴 수 있는 땅은 정해져 있다.

1 : 하얀색 : 배양액을 뿌릴 수 없음
2 : 황토색 : 배양액을 뿌릴 수 있음
0 : 하늘색 : 호수

- 초록색 배양액과 빨간색 배양액이 동일한 시간에 도달한 땅에서는 두 배양액이 합쳐져서 꽃이 핌
- 꽃이 피어난 땅에서는 배양액이 사라지기 때문에 인접한 땅으로 배양액 퍼트리지 않음

- 배양액 : 매초 마다 이전에 배양액이 도달한 적이 없는 인접한 땅으로 퍼져나감


'''
def comb(idx, select):
    if len(select) == g+r:
        print(select)
        return

    for i in range(idx, len(배양액num)):
        comb(i+1, select+[배양액num[i]])

n,m,g,r = map(int,input().split())

garden = [list(map(int,input().split())) for _ in range(n)]

# 배양액을 뿌릴 수 있는 곳을 담기
배양액idx = []
for i in range(n):
    for j in range(m):
        if garden[i][j] == 2:
            배양액idx.append([i,j])

# 리스트 갯수
배양액num = [x for x in range(len(배양액idx))]

# 조합 갯수에 맞춰서 뽑아오기
comb(0,[])
'''
보석 도둑

보석이 총 N개
무게 M과 가격 V를 가지고 있음
가방을 K개 가지고 있고,
가방에 담을 수 있는 최대 무게 C

가방에는 최대 한 개의 보석만 넣을 수 있음

상덕이가 훔칠 수 있는 보석의 최대 가격을 구하여라

풀이
- 각 가방에 담을 수 있는 최대 가치의 보석을 담되 용량이 작은 가방부터 보석을 담는다.
- 가방의 순서를 신경쓰지 않고 보석을 담는다면 보석을 담지 못하는 경우가 생김
예를들어
보석 : [(1,20), (2,100), (5,50)]
가방 : [10, 2]
 -> 가방을 용량의 오름차순으로 정렬했을 때
 -> 각 가방에 담을 수 있는 모든 보석을 찾을 때 최소힙 사용
 -> 각 가방에 넣을 수 있는 보석 중 가장 가치가 큰 보석을 찾을 때 최대힙 이용
'''

import sys
import heapq  # 힙

input = sys.stdin.readline  # 입력 빠르게

n, k = map(int, input().split())
gems = [[*map(int, input().split())] for _ in range(n)]
bags = [int(input()) for _ in range(k)]

gems.sort()  # 무게 오름차순, 무게 같으면 가격 오름차순
bags.sort()  # 가방 무게 오름차순
result = 0  # 결과 출력값 초기화
tmp = []  # 보석의 가격 저장 리스트

for bag in bags:  # 각 가방 무게에 대해
    while gems and gems[0][0] <= bag:  # 제일 가벼운 보석무게를 bag이 허용하는한 반복
        heapq.heappush(tmp, -gems[0][1])  # 가격을 최대힙에 저장(음수로 저장하여 최소힙을 최대힙으로)
        heapq.heappop(gems)  # 가격 저장한 보석은 버리기
    if tmp:  # bag 무게 이하 보석 가격 다 저장했으면
        result -= heapq.heappop(tmp)  # 제일 가치가 높은 가격 더하기(음수니까 빼기)
print(result)
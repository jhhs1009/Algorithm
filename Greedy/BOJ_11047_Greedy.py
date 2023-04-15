'''
동전 0

준규가 가지고 있는 동전은 총 N개
매우 많이 가지고 있음
동전을 적절히 사용해서 그 가치의 합을 k로 만들려고 함
필요한 동전 개수의 최솟값을 구하는 프로그램 작성
'''
n,k = map(int,input().split())

money = [int(input()) for _ in range(n)]
cnt = 0

while True:
    if k == 0:
        print(cnt)
        break

    for i in range(len(money)-1,-1,-1):
        if money[i]<=k:
            cnt += k//money[i]
            k %= money[i]
            break

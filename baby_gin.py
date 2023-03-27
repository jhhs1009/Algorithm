num = int(input())
c = [0] * 12 # 대충 가장 큰 숫자보다 1개 더 크게 만들면 됨 근데 커봤자 9니까 12개쯤

for i in range(6):
    c[num%10] += 1 # c의 인덱스 번호에 1더하기
    num //= 10
'''
print(c)
[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
'''

i = 0
tri = run = 0
while i < 10: # i+2까지 조사를 할 꺼니까 2개 작은 값으로 범위 설정
    if c[i] >=3: #트리플 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >=1 and c[i+2] >=1: #런 조사후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print("baby-gin 이다!")
else:
    print("baby-gin이 아니다!")
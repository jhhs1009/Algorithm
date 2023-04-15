'''
대회 or 인턴

2명의 여학생과 1명의 남학생이 팀을 결성해서 나가는 것이 원칙

N명의 여학생
M명의 남학생
K명은 반드시 인턴쉽 프로그램에 참여해야 함

만들 수 있는 최대의 팀 수를 구하기
'''

n,m,k = map(int,input().split())

# 2명의 여학생과 1명의 남학생은 필수로 있어야 함
cnt = 0
while True:
    n-=2
    m-=1

    if n<0 or m<0 or(n+m)<k:
        break
    cnt += 1

print(cnt)
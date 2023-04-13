'''
백준 1461 도서관 - 골드 5

현재 0에 위치
책도 0에 위치

최소 걸음 수 계산
책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다.
모두 놔두지 않았다면 다시 0으로 돌아야함
한번에 최대 M권의 책을 들 수 있다.

-39 -37 -29 -28 -6 2 11
'''
n,m = map(int,input().split())

book = list(map(int,input().split()))

# 크기 순으로 정렬
book = sorted(book)

# 가장 큰 값 찾기
ma = max(abs(book[0]), abs(book[-1]))

res = 0
if n%m==0:
    for i in range(0,n,m):
        음수 = 0
        양수 = 0
        a = book[i:i+m]
        for j in range(m):
            if a[j]<0:
                음수+=1
            elif a[j]>0:
                양수+=1
        if 음수 == m or 양수 == m:
            if a[0] == ma or a[-1]==ma:
                res += ma
            else:
                if 음수 == m:
                    res += abs(a[0])*2
                elif 양수 == m:
                    res += abs(a[-1])*2
        else:
            tmp_plus = []
            tmp_sub = []
            for k in range(m):
                if a[k]<0:
                    tmp_sub.append(a[k])
                elif a[k]>0:
                    tmp_plus.append(a[k])
            if tmp_sub:
                res += abs(tmp_sub[0])*2
            if tmp_plus:
                res += (tmp_plus[-1])*2
else:
    # 양수 음수 나누기
    tmpup = []
    tmpdown = []
    for i in range(n):
        if book[i]<0:
            tmpdown.append(book[i])
        elif book[i]>0:
            tmpup.append(book[i])
    for i in range(0,len(tmpdown)-len(tmpdown)%m,m):
        a = tmpdown[i:i+m]
        if abs(a[0])==ma:
            res += abs(a[0])
        else:
            res += abs(a[0])*2
    a = tmpdown[len(tmpdown)-len(tmpdown)%m:len(tmpdown)]
    if a:
        if abs(a[0])==ma:
            res += abs(a[0])
        else:
            res += abs(a[0])*2
    for i in range(len(tmpup),0+len(book)%m,-m):
        a = tmpup[i-m:i]

        if abs(a[-1])==ma:
            res += a[-1]
        else:
            res += a[-1]*2
    a = tmpup[0:len(tmpup)%m]
    if a:
        if a[-1]==ma:
            res += a[-1]
        else:
            res += a[-1]*2
print(res)
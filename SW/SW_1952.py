'''
수영장에서 판매하고 있는 이용권

1. 1일 이용권 : 1일 이용이 가능함
2. 1달 이용권 : 1달 동안 이용이 가능함, 매달 1일부터 시작
3. 3달 이용권 : (연속된 3달 동안 이용이 가능, 매달 1일부터 시작)
4. 1년 이용권 : 1년 동안 이용이 가능함, 매년 1월 1일부터 시작함

각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때,
가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고
그 비용을 정답으로 출력하는 프로그램을 작성하라
'''

def b(i,res):
    global answer
    if month[i] == month[-1]:
        if answer > res:
            answer = res
        return
    if res>answer:
        return
    b(i+1, res+(plan[month[i]]*money[0]))
    b(i+1, res+(1*money[1]))

    if len(month)-4>=i:
        cnt = 0
        for j in range(len(month)-1):
            if month[j] + 1 == month[j+1]:
                cnt += 1
        if cnt >= 2:
            b(i+3, res+(money[2]))

    if len(month)-1 == i:
        b(len(month)-1, res+(1*money[3]))



T = int(input())

for tc in range(T):
    money = list(map(int,input().split()))
    plan = list(map(int,input().split()))

    month = []

    for i in range(12):
        if plan[i] != 0:
            month.append(i)
    month = month + [99]
    answer = 99999
    b(0,0)
    print(f"#{tc+1} {answer}")


'''
햄버거 다이어트

햄버거 재료에 대한 점수와
가게에서 제공하는 재료에 대한 칼로리가 주어졌을 때
좋아하는 햄버거를 먹으면서도 다이어트에 성공할 수 있도록
정해진 칼로리 이하의 조합 중에서
선호하는 햄버거를 조합해주는 프로그램을 만들어 보자

'''

def b(idx, res, c):
    global answer

    if res>l:
        return

    if idx>=n:
        if answer < c:
            answer = c
        return

    b(idx+1,res+(c_list[idx][1]),c+(c_list[idx][0]))
    b(idx+1,res,c)



T = int(input())

for tc in range(T):
    n,l = map(int,input().split())
    c_list = [list(map(int,input().split())) for _ in range(n)]

    # 재귀 돌릴까.
    # 조합 써서 가장 많이 어쩌구 하면 흠
    res = 0
    answer = 0
    c = c_list[0][0]
    b(0,res,0)
    print(f"#{tc+1} {answer}")
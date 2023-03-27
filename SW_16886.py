'''
전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야함
사무실에서 출발해 각 구역을 한번씩만 방문하고
사무실로 돌아올 때의 최소 배터리 사용량을 구하시오

배터리 사용량은 표로 제공
1번 : 사무실
2번 ~ N번 : 관리구역 번호

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

예)
N이 3인 경우 : 1-2-3-1, 1-3-2-1
위의 경로로 가능 하다.

1로 시작해서 1로 돌아와야 함

풀이
- 가로 먼저
- 시작점이 2개가 존재 ( 1행의 숫자가 있는 자리는 시작 가능 )
- 만약에 [1][2]를 선택하면 이제 [2]열은 선택 불가능,
'''
# 순열 구하기

def solve(i):
    global minV
    if i == n - 2:
        tmp = get_result(arr)
        if tmp < minV:
            minV = tmp
        return

    for j in range(i, n - 1):
        arr[i], arr[j] = arr[j], arr[i]
        solve(i + 1)
        arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for i in range(T):
    n = int(input())
    num_list = [list(map(int,input().split())) for _ in range(n)]

    for i in range(n):
        if num_list[0][i] != 0:
            r,c = 0,i
            ans = dfs(r,c)
            print(ans)


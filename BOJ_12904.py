'''
A와 B

두 문자열 S와 T가 주어졌을 때,
S를 T로 바꾸는 게임

* 문자열의 뒤에 A를 추가함
* 문자열을 뒤집고 뒤에 B를 추가함

주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지!
'''

S = list(input())
T = list(input())

res = 0
while T:
    if S == T:
        res = 1
        break
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()
else:
    res = 0
print(res)

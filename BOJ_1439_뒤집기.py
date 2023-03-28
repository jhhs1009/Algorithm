'''
0과 1로만 이루어진 문자열 S를 가지고 있다.

다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 함

다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 뒤집는 것

뒤집는 것)
* 1 - 0
* 0 - 1

뒤집는 행동의 최소 횟수를 출력하시오
'''

s = input()
s += "3"
one = 1
zero = 1
dic = {'zero': 0, 'one':0}

for i in range(len(s)-1):
    if s[i] == "0":
        if s[i] == s[i+1]:
            zero += 1
        else:
            dic['zero'] += 1
            zero = 1
    else:
        if s[i] == s[i+1]:
            one += 1
        else:
            dic['one'] += 1
            one = 1
if dic['one']>=dic['zero']:
    print(dic['zero'])
else:
    print(dic['one'])






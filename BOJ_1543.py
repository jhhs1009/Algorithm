'''
어떤 단어가 총 몇 번 등장하는지 세려고 함

세준이의 함수는 중복되어 세는 것은 빼고 세야함

예를 들어, 문서가 abababa이고, 찾으려는 단어가 ababa라면,
세준이의 이 함수는 이 단어를 0번부터 찾을 수 있고
2번부터도 찾을 수 있다.
그러나 동시에 셀 수는 없다.

'''

s1 = input()
s2 = input()

cnt = 0
i = 0

while i<=len(s1)-len(s2):
    if s1[i:i+len(s2)] == s2:
        cnt += 1
        i += len(s2)
    else:
        i += 1
print(cnt)
'''
숫자의 신

오세준은 지금 k개의 자연수를 가지고 있음
k개의 수 중에 정확하게 N개의 수를 뽑아내서 그 수를 붙여서 만들 수 있는 수 중에 가장 큰 수를 만들고자 한다.
같은 수를 여러 번 이용 가능

이 수를 적어도 한 번 이상 이용해서 만들 수 있는 수 중에 가장 큰 수를 출력하라

예를 들어 2,3,7 이라는 3개의 수를 가지고 있고
4개의 수를 뽑아야 한다면
7732를 만들면 가장 큰 수가 된다.

- 풀이
버블소트를 하기전에 큰 수를 뽑아
버블소트를 해 큰수 만들기처럼

그 숫자랑 큰 수로 또 버블소트를 해
'''

def bubble(numbers):
    for i in range(n-1):
        for j in range(0,n-1):
            tmp = str(numbers[j])+str(numbers[j+1])
            tmp2 = str(numbers[j+1])+str(numbers[j])
            if int(tmp)<int(tmp2):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers

k,n = map(int,input().split())

num = [int(input()) for _ in range(k)]

m = max(num)

num += [str(m)]*(n-k)
bubble(num)
print("".join(map(str,num)))


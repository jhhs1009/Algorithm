'''
큰 수 만들기

'''
def bubble(numbers):
    for i in range(T-1):
        for j in range(0,T-1):
            tmp = numbers[j]+numbers[j+1]
            tmp2 = numbers[j+1]+numbers[j]
            if int(tmp)<int(tmp2):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers


T = int(input())
numbers = list(input().split())
bubble(numbers)
tmp = ''.join(map(str,numbers))
print(int(tmp))
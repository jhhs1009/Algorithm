# 10진수 -> n진수

def convert_iter(num, base):
    power = 0
    tmp = ''
    while num:
        tmp = str(num%base) + tmp
        num //= base
    return tmp

convert_iter(16,2)
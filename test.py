from itertools import combinations_with_replacement

nums = [i for i in range(1,5)]
m = 2

case = combinations_with_replacement(nums, m)
print(list(case))

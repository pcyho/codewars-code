import math


def find(m, n):
    result = []
    for i in range(m, n + 1):
        if fun(i) != None:
            result.append(fun(i))
    return result


def fun(num):
    lis = []
    for i in range(1, num + 1):
        if num % i == 0:
            lis.append(i)
    list1 = [n**2 for n in lis]
    return [num, sum(list1)] if int(math.sqrt(sum(list1)))**2 == sum(list1) else None


print(find(42, 250))
# 优化

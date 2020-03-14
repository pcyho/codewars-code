import operator

n = 39

while len(str(n)) > 1:
    a = list(str(n))
    n = 1
    for each in a:
        n *= int(each)
print(n)


def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        i += 1
    return i

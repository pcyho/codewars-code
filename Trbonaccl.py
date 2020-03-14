def Tribonaccl(n, m):
    a, b, c = n[0], n[1], n[2]
    i = 1
    while i < m:
        i += 1
        a, b, c = b, c, a + b + c
        yield a


print([0] + list(Tribonaccl([0, 0, 1], 10)))


def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res

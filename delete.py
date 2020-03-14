def delete_digit(n):
    a = list(str(n))
    b = a
    print(b.append(sum([int(each)**2 for each in b])))
    # while len(b) > 1 and b[0] != b[-1]:
    #b.append(''.join([sum([int(each)**2 for each in b[-1]])]))
    # return max([int(list(str(n)).del(each)) for each in range(0, len(str(n)))])


print(delete_digit(233))

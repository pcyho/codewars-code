def wholikeit(names):
    if len(names) == 0:
        return "no one names this"
    elif len(names) == 1:
        return "{0} names this".format(names[0])
    elif len(names) == 2:
        return "{0} and {1} like this".format(names[0], names[1])
    elif len(names) == 3:
        return "{0}, {1} and {2} like this".format(names[0], names[1], names[2])
    else:
        return "{0}, {1} and {2} others like this".format(names[0], names[1], len(names) - 2)


list = ["Alex", "Jacob", "Mark", "Max"]
print(wholikeit(list))


def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n - 2)

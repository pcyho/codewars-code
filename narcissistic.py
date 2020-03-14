def narcissistic(value):
    return True if sum([int(each)**len(list(str(value))) for each in list(str(value))]) == value else False


print(narcissistic(7))

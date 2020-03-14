# coding: utf-8
"""
this program is to be given a nummber list and return the most bigger nummbers order
"""

# test_list = ["352", "351", "325", "498", "1111", "12", "1", "2", "23424"]
test_list = []
while True:
    in_nun = input("请输入第{}个数，或输入 y 开始计算。".format(len(test_list) + 1))
    if in_nun == "y":
        break
    elif in_nun.isdigit() == True:
        test_list.append(in_nun)
    else:
        raise ValueError()

print("your input nums: ", test_list)


def return_sort_dic(dic, reverse):
    """
    :param dic: input dict
    :param reverse: should be True
    :return: a list
    """
    data = [{k: v} for k, v in dic.items()]
    f = lambda x: list(x.values())[0]
    return sorted(data, key=f, reverse=reverse)


def get_weight(str):
    """
    this func is to caculate the weight of each number (type str), we sort each number according to it's weights
    the way of caculate:
        for example: "231" is 2+(3-2)*0.1+(1-3)*0.01=2.08
                     "0"   is 0
    :param str:  the number (type str)
    :return: weights(type float)
    """
    weight = 0
    for _ in range(0, len(str)):
        if _ is 0:
            weight += int(str[_])
        else:
            weight += (int(str[_]) - int(str[_ - 1])) / (10 ** _)
    return weight


d = {}
for i in test_list:
    d[i] = get_weight(i)
r = return_sort_dic(d, True)
result = "".join([list(r[i].keys())[0] for i in range(0, len(r))])
print("the result of program is:", result)

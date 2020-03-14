import re

input = """1000.00!=
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10
"""

start = float(re.search(r"^[0-9|/.]+", input).group())
lines = input.split('\n')[1:-1]
a = [" Balance " + str(round((start - float(re.search(r"[0-9|/.]+$", each).group(0))), 2)
                       ) + "\n" for each in lines]
result = ""
for f, l in zip(lines, a):
    result += f + l
result = ("Original Balance: %.2f" % start) + "\n" + result
print(result)

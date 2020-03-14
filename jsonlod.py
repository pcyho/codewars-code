import json
import os

with open('E:\\Program\\python\\USCities.json', 'rb') as f1:
    with open('E:\\Program\\python\out.txt', 'w') as f2:
        a = json.loads(f1.read())
        print(type(a))
        for each in a:
            f2.write(str(each) + '\n')

import threading
import time

start = time.clock()

num = [-5, 3, 9, 11, -1, 3, 12, 0, 8, -3, 23, 5, 19]


def doSleep(func):
    co = 0.02
    time.sleep(co * pow(1.1, float(func)))
    print(func)


thread_list = []
for i in range(len(num)):
    temp = threading.Thread(target=doSleep, args=(str(num[i]), ))
    thread_list.append(temp)

if __name__ == '__main__':
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    end = time.clock()
    print('it takes', str(end - start))

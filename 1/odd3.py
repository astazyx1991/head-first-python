from datetime import datetime
import time
import random

#判断10次当前系统时间是奇数还是偶数
#每次间隔时间1到61秒
odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19, 21,
        23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43,
        45, 47, 49, 51, 53, 55, 57, 59]
for i in range(10):
    if datetime.today().minute in odds:
        print("this is odd")
    else:
        print("not odd")
    time.sleep(random.randint(1, 61))
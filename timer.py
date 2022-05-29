import time
from datetime import datetime
from threading import Timer


def timer_1(list_1):
    list_1.pop(2)
    list_1 = [int(i) for i in list_1]

    time_1 = int(str(list_1[0]) + str(list_1[1])) * 3600 + int(str(list_1[2]) + str(list_1[3])) * 60
    time_2 = datetime.now().hour * 3600 + datetime.now().minute * 60

    time.sleep(time_1 - time_2)
    return True
import multiprocessing
from multiprocessing import Process
from .client1 import *
from .client2 import *
from .client3 import *




def fun_call1():
    print('Client 1 call')
    data_1 = Server1()
    print(type(data_1))
    return data_1


def fun_call2():
    print('Client 2 call')
    data_2 = Server2()
    print(type(data_2))
    return data_2


def fun_call3():
    print('Client 3 call')
    data_3 = Server3()
    print(type(data_3))
    return data_3


# def Main():
#     p1 = Process(target=fun_call1())
#     p2 = Process(target=fun_call2())
#     p3 = Process(target=fun_call3())
#     p1.start()
#     p2.start()
#     p3.start()
#     p1.join()
#     p2.join()
#     p3.join()
    # manager = multiprocessing.Manager()


# if __name__ == '__main__':
#     Main
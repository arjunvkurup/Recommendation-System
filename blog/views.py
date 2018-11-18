from django.shortcuts import render
from django.template import loader, Context
from geopy.geocoders import GoogleV3
# from ..utils.client1 import *
# from ..utils.client2 import *
# from ..utils.client3 import *
from ..utils.parallel import *
from multiprocessing import Process



# Create your views here.
def index(request):
    template = loader.get_template('blog/index.html')

    data_1
    data_2
    data_3

    def fun_call1():
        print('Client 1 call')
        global data_1
        data_1 = Server1()
        print(data_1)

    def fun_call2():
        print('Client 2 call')
        global data_2
        data_2 = Server2()
        print(data_2)

    def fun_call3():
        print('Client 3 call')
        global data_3
        data_3 = Server3()
        print(data_3)

    p1 = Process(target=fun_call1())
    p2 = Process(target=fun_call2())
    p3 = Process(target=fun_call3())
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()



    # LongLatCount1 =
    # LongLatCount2 = parallel.data_2
    # LongLatCount3 = parallel.data_3
    LongLatCount1 = [
        [[-159.38, 22.08], 74],
        [[-157.83, 21.31], 807],
        [[-156.54, 20.9], 0],
        [[-158.01, 21.54], 0],
        [[-158.0, 21.38], 495],
        [[-159.56, 21.93], 10],
        [[-156.05, 20.75], 0],
        [[-156.36, 20.81], 28],
        [[-158.17, 21.43], 98],
        [[-157.75, 21.37], 22]
    ]
    LongLatCount2 = [
        [[-159.38, 22.08], 74],
        [[-157.83, 21.31], 807],
        [[-156.54, 20.9], 0],
        [[-158.01, 21.54], 0],
        [[-158.0, 21.38], 995],
        [[-159.56, 21.93], 10],
        [[-156.05, 20.75], 0],
        [[-156.36, 20.81], 28],
        [[-158.17, 21.43], 98],
        [[-157.75, 21.37], 22]
    ]
    LongLatCount3 = [
        [[-159.38, 22.08], 74],
        [[-157.83, 21.31], 7],
        [[-156.54, 20.9], 0],
        [[-158.01, 21.54], 0],
        [[-158.0, 21.38], 5],
        [[-159.56, 21.93], 10],
        [[-156.05, 20.75], 0],
        [[-156.36, 20.81], 28],
        [[-158.17, 21.43], 98],
        [[-157.75, 21.37], 22]
    ]
    max1 = LongLatCount1[0][1]
    max_index1 = 0
    for i in range(len(LongLatCount1)):
        # print(LongLatCount1[i][1])
        if LongLatCount1[i][1] >= max1:
            max1 = LongLatCount1[i][1]
            max_index1 = i
    max2 = LongLatCount2[0][1]
    max_index2 = 0
    for i in range(len(LongLatCount2)):
        # print(LongLatCount1[i][1])
        if LongLatCount2[i][1] >= max2:
            max2 = LongLatCount2[i][1]
            max_index2 = i
    max3 = LongLatCount3[0][1]
    max_index3 = 0
    for i in range(len(LongLatCount3)):
        # print(LongLatCount1[i][1])
        if LongLatCount3[i][1] >= max3:
            max3 = LongLatCount3[i][1]
            max_index3 = i
    best = [[0,0],0]
    if LongLatCount1[max_index1][1] > LongLatCount2[max_index2][1]:
        if LongLatCount1[max_index1][1] > LongLatCount3[max_index3][1]:
            best = LongLatCount1[max_index1]
    elif LongLatCount2[max_index2][1] > LongLatCount3[max_index3][1]:
        best = LongLatCount2[max_index2]
    else:
        best = LongLatCount1[max_index1]
    geolocator = GoogleV3(api_key='AIzaSyA2OkaAMXQ7o0kXBpTI2LQMDCV0UKGV0Z0')
    # point = '"' + best[0][0] + "," + best[0] "'"
    best_l = geolocator.reverse('"' + str(best[0][1]) + ',' + str(best[0][0]) + '"')
    best_l2 = geolocator.reverse('"' + str(LongLatCount2[max_index2][0][1]) + ',' + str(LongLatCount2[max_index2][0][0]) + '"')
    best_l1= geolocator.reverse('"' + str(LongLatCount1[max_index1][0][1]) + ',' + str(LongLatCount1[max_index1][0][0]) + '"')
    best_l3 = geolocator.reverse(
        '"' + str(LongLatCount3[max_index3][0][1]) + ',' + str(LongLatCount3[max_index3][0][0]) + '"')
    return render(request, 'blog/index.html', {'LongLat1': LongLatCount1[max_index1],
                                               'LongLat2': LongLatCount2[max_index2],
                                               'LongLat3': LongLatCount3[max_index3],
                                               'Site1': LongLatCount1,
                                               'Site2': LongLatCount2,
                                               'Site3': LongLatCount3,
                                               'best': best,
                                               'best_l': best_l[0],
                                               'best_l1': best_l1[0],
                                               'best_l2': best_l2[0],
                                               'best_l3': best_l3[0]})

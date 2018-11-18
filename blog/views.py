from django.shortcuts import render
from django.template import loader
from geopy.geocoders import GoogleV3
from .utils import parallel


# Create your views here.
def index(request):
    template = loader.get_template('blog/index.html')

    # def cal_1():
    LongLatCount1 = parallel.fun_call1()


    # def cal_2():
    LongLatCount2 = parallel.fun_call2()


    # def cal_3():
    LongLatCount3 = parallel.fun_call3()


    # p1 = Process(target=cal_1())
    # p2 = Process(target=cal_2())
    # p3 = Process(target=cal_3())
    # p1.start()
    # p2.start()
    # p3.start()
    # p1.join()
    # p2.join()
    # p3.join()


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

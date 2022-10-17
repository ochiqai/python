import matplotlib.pyplot as plt
import numpy as np
from vector_taq_01 import vector_taq


def mat2list(matritsa):
    _list = []
    for kanal in range(3):
        for i in range(50):
            for j in range(50):
                _list.append(matritsa[i,j,kanal])
    return _list



yuz_rasmlar = []
for i in range(24):
    joy = "./rasmlar/yuz_rasm_{}.jpg".format(i)
    y = plt.imread(joy) / 255
    # matritsani vectorga o'tkazish
    _l = mat2list(y)
    yuz_rasmlar.append(_l)

print(yuz_rasmlar.__len__())


asosiy_rasm = yuz_rasmlar[0]
for i in range(23):
    yaqinlik = vector_taq(asosiy_rasm, yuz_rasmlar[i+1])
    print(i, yaqinlik)






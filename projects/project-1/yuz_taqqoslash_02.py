import cv2
import numpy as np
from insightface.app import FaceAnalysis
from vector_taq_01 import vector_taq


def rasm_ol(joy):
    rasm = cv2.imread(joy)
    return rasm


app = FaceAnalysis(allowed_modules=['detection', 'recognition'])
app.prepare(ctx_id=0, det_size=(640, 640))

rasm = rasm_ol('data/yuz.png')

yuzlar = app.get(rasm)

yuz_rasmlar = []
for idx, yuz in enumerate(yuzlar):
    # koor = yuz['bbox']
    yuz_rasmlar.append(yuz['embedding'])

    # x1, y1, x2, y2 = int(koor[0]), int(koor[1]), int(koor[2]), int(koor[3])
    # yuz_rasm = rasm[y1:y2, x1:x2]

    # yuz_rasm = cv2.resize(yuz_rasm, (50, 50))
    # cv2.imwrite("rasmlar2/yuz_rasm_{}.jpg".format(idx), yuz_rasm)


asosiy_rasm = yuz_rasmlar[0]
uxshashlar = []
for i in range(24):
    yaqinlik = vector_taq(asosiy_rasm, yuz_rasmlar[i])
    yaqinlik = round(yaqinlik, ndigits=3)
    print(i, yaqinlik)
    uxshashlar.append(yaqinlik)
np.savez("natija/ml_natija", ai_usul=uxshashlar)



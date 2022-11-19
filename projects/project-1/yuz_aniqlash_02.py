import cv2
from insightface.app import FaceAnalysis
import matplotlib.pyplot as plt


def rasm_ol(joy):
    rasm = cv2.imread(joy)
    return rasm

app = FaceAnalysis(allowed_modules='detection')
app.prepare(ctx_id=0, det_size=(640, 640))

rasm = rasm_ol('yuz.png')

yuzlar = app.get(rasm)
rimg = app.draw_on(rasm, yuzlar)
cv2.imwrite("./yuzlar_natija.jpg", rimg)

for idx, yuz in enumerate(yuzlar):
    koor = yuz['bbox']
    x1, y1, x2, y2 = int(koor[0]), int(koor[1]), int(koor[2]), int(koor[3])
    yuz_rasm = rasm[y1:y2, x1:x2]
    # yuz_rasm = yuz_rasm[:, :, ::-1]

    yuz_rasm = cv2.resize(yuz_rasm, (50, 50))
    cv2.imwrite("rasmlar/yuz_rasm_{}.jpg".format(idx), yuz_rasm)

    # plt.imshow(yuz_rasm)
    # plt.show()








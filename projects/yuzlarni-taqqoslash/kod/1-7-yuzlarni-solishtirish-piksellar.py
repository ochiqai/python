import cv2
import insightface
from insightface.app.common import Face
from insightface.app import FaceAnalysis
import matplotlib.pyplot as plt
import math
import numpy as np

# app = FaceAnalysis()
# /home/ochiqai/.insightface/models/buffalo_l/det_10g.onnx

model_joyi = "/home/ochiqai/.insightface/models/buffalo_l/det_10g.onnx"
yuz_aniqlagich = insightface.model_zoo.get_model(model_joyi)
# (640, 640) ixtiyoriy kiritilgan rasmni ushbu o'lchamga o'tkazadi.
yuz_aniqlagich.prepare(ctx_id=0, input_size=(640, 640))

rasm_joyi = "rasmlar/uz_prez.jpg"
rasm = cv2.imread(rasm_joyi) # [0, 255]

yuz_koordinatalari, yuz_qismlari = yuz_aniqlagich.detect(rasm)

yuz_koordinatalari_uzgartirilgan = []
for i in range(yuz_koordinatalari.shape[0]):
    koordinata = yuz_koordinatalari[i, 0:4]
    ishonch = yuz_koordinatalari[i, 4]
    yuz_qism = yuz_qismlari[i]

    yuz = Face(bbox=koordinata, kps=yuz_qism, det_score=ishonch)
    yuz_koordinatalari_uzgartirilgan.append(yuz)


app = FaceAnalysis()
chizilgan_rasm = app.draw_on(rasm, yuz_koordinatalari_uzgartirilgan)

chizilgan_rasm = cv2.cvtColor(chizilgan_rasm, cv2.COLOR_BGR2RGB)
# plt.imshow(chizilgan_rasm)
# plt.show()

## piksellarni olish
rasm = cv2.cvtColor(rasm, cv2.COLOR_BGR2RGB)
yuz_koordinatalari_piksellar = []
for y in yuz_koordinatalari_uzgartirilgan:
    x1 = int(y["bbox"][0])
    y1 = int(y["bbox"][1])
    x2 = int(y["bbox"][2])
    y2 = int(y["bbox"][3])
    rasm_y = rasm[y1:y2, x1:x2]
    rasm_y = cv2.resize(rasm_y, (50, 50))
    piksellar = rasm_y.reshape((1, 7500)) # matrixdan vectorga o'tdik
    yuz_koordinatalari_piksellar.append([piksellar, rasm_y])

# rasmlarni chiqaramiz
# for yuz in yuz_koordinatalari_piksellar:
#     piksel, rasm = yuz[0], yuz[1]
#     plt.imshow(rasm)
#     plt.show()


# test rasmni o'qish
rasm_joyi = "rasmlar/test_prez.jpg"
test_rasm = cv2.imread(rasm_joyi) # [0, 255]
test_rasm = cv2.resize(test_rasm, (50, 50))
test_piksellar = test_rasm.reshape((1, 7500))


def ildiz(x):
    return math.sqrt(x)


def vector_taq(a, b):
    # kosinus o'xshashlik https://en.wikipedia.org/wiki/Cosine_similarity
    # 1*1 + 2*2 + 2*2 + 1*2 + 1*1 + 1*1

    if len(a) == len(b):
        i = 0
        v = 0
        while i < len(a):
            v += (a[i] * b[i])
            i += 1

        # modul
        i = 0
        modul_a = 0
        modul_b = 0
        while i < len(a):
            modul_a += (a[i] * a[i])
            modul_b += (b[i] * b[i])
            i += 1

        modul_a = ildiz(modul_a)
        modul_b = ildiz(modul_b)
        maxraj = modul_a * modul_b
        yaqinlik = v / maxraj

        return yaqinlik
    else:
        print("Elementlar soni teng bo'lish kerak!")


for yuz in yuz_koordinatalari_piksellar:
    piksellar_bazadagi = yuz[0]
    yaqinlik = vector_taq(test_piksellar.tolist()[0], piksellar_bazadagi.tolist()[0])
    plt.imshow(yuz[1])
    if yaqinlik > 0.855:
        plt.title("Bu Shavkat Mirziyoyev")
    else:
        plt.title("Bu boshqa odam")
    plt.show()



























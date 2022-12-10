import cv2
import insightface
from insightface.app.common import Face
from insightface.app import FaceAnalysis
import matplotlib.pyplot as plt


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
plt.imshow(chizilgan_rasm)
plt.show()



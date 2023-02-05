import math
import cv2
import insightface
from insightface.app.common import Face
from insightface.app import FaceAnalysis
import numpy as np
import os



def ildiz(x):
    """
    Sonni ildizini oladi, masalan: 49 bersak, 7 qaytadi
    """
    return math.sqrt(x)


def surat(a, b):
    """
    a va b listlarni olib elementlarini bir biriga
    ko'paytirib qo'shamiz.

    Parameters
    ----------
    a : list
    b : list

    Returns
    -------
    float
        yig'indi
    """
    kasr_surati, i = 0, 0
    while i < len(a):
        kasr_surati += (a[i] * b[i])
        i += 1
    return kasr_surati


def maxraj(a, b):
    """
    a va b listni olib, har birining modulini olib, ularni
    ko'paytmasini qaytaramiz
    Parameters
    ----------
    a : list
    b : list

    Returns
    -------
    float
        ko'paytma
    """
    i = modul_a = modul_b = 0
    while i < len(a):
        modul_a += (a[i] * a[i])
        modul_b += (b[i] * b[i])
        i += 1

    modul_a = ildiz(modul_a)
    modul_b = ildiz(modul_b)
    kasr_maxraji = modul_a * modul_b
    return kasr_maxraji


def vector_taq(a, b):
    """
    Bu funksiya 2 ta listni taqqoslaydi. Taqqoslash kosinus teoremasi
    asosida. Yoki  boshqacha nomda kosinus o'xshashlik:
    https://en.wikipedia.org/wiki/Cosine_similarity

    Parameters
    ----------
    a : list
        birinchi list
    b : list
        ikkinchi list

    Returns
    -------
    float
        berilgan vektorlar yaqinligini qaytaradi
    """

    if len(a) == len(b):
        yaqinlik = surat(a, b) / maxraj(a, b)
        return yaqinlik
    else:
        print("Elementlar soni teng bo'lish kerak!")


def aniqlash(model, rasm):
    """
    Berilgan rasmni kordinatasini aniqlaydi

    Parameters
    ----------
    model: class 'insightface.model_zoo.retinaface.RetinaFace'
        aniqlagich model (detection)
    rasm: class 'numpy.ndarray'

    Returns
    -------
    list
        aniqlangan yuzning kordinatalari
    """
    kordinatalar, landmarklar = model.detect(rasm)

    kordinatalar_format = []
    for i in range(kordinatalar.shape[0]):
        koordinata = kordinatalar[i, 0:4]
        ishonch = kordinatalar[i, 4]
        yuz_qism = landmarklar[i]

        yuz = Face(bbox=koordinata, kps=yuz_qism, det_score=ishonch)
        kordinatalar_format.append(yuz)

    return kordinatalar_format[0]


def model_yuklash(turi):
    """
    Tur bo'yicha modelni qaytaradi
    Parameters
    ----------
    turi : str
        model turi
    Returns
    -------
    model:
        berilgan tur bo'yicha modelni qaytaradi
    """
    home = os.path.expanduser('~')

    if not os.path.exists(os.path.join(home, ".insightface")):
        _ = FaceAnalysis()

    if turi == 'aniqlagich':
        joyi = os.path.join(
            home,
            ".insightface/models/buffalo_l/det_10g.onnx"
        )
        aniqlagich = insightface.model_zoo.get_model(joyi)
        # (640, 640) ixtiyoriy kiritilgan rasmni ushbu o'lchamga o'tkazadi.
        aniqlagich.prepare(ctx_id=0, input_size=(640, 640))
        return aniqlagich

    elif turi == 'embedding':
        joy = os.path.join(
            home,
            ".insightface/models/buffalo_l/w600k_r50.onnx"
        )
        embedding = insightface.model_zoo.get_model(joy)
        embedding.prepare(ctx_id=0)
        return embedding
    else:
        print("Bunaqa model yo'q.")


def chizish(rasm, kordinatalar):
    """
    Berilgan rasmni olib unga berilgan kordinatalar asosida
    to'rtburchak va landmarklarni chizadi.
    To'rtburchak: (x1,y1), (x2,y2)
    Landmark: 5 ta kordinatam yuz qismlar (landmark) uchun (2 ta ko'z, lab 2 chekasi, burun)

    Parameters
    ----------
    rasm : numpy
    kordinatalar : list

    Returns
    -------
    numpy
        kordinatalar chizilgan rasm
    """
    chizilgan_rasm = _chizish(rasm, kordinatalar)
    # BGR --> RGB
    # chizilgan_rasm = cv2.cvtColor(chizilgan_rasm, cv2.COLOR_BGR2RGB)
    return chizilgan_rasm


def _chizish(rasm, faces):
    """

    Parameters
    ----------
    rasm: numpy
    faces: list

    Returns
    -------

    """
    if type(faces) != list:
        faces = [faces]
    chimg = rasm.copy()

    for i in range(len(faces)):
        face = faces[i]
        box = face.bbox.astype(np.int_)
        color = (0, 0, 255)
        cv2.rectangle(chimg, (box[0], box[1]), (box[2], box[3]), color, 2)
        if face.kps is not None:
            kps = face.kps.astype(np.int_)
            for l in range(kps.shape[0]):
                color = (0, 0, 255)
                if l == 0 or l == 3:
                    color = (0, 255, 0)
                cv2.circle(chimg, (kps[l][0], kps[l][1]), 1, color, 2)
    return chimg

def embedding_olish(model, rasm, kordinatalar):
    """
    Berilgan rasm va kordinatralar asosida, embeddinglarni oladi
    Parameters
    ----------
    embedding_model : model
    rasm : numpy
    kordinatalar : list

    Returns
    -------
    list
    embeddinglar qaytariladi
    """
    # rasmdan yuzlar qirqib olinib, yuzlar listiga yuklandi
    rasm = cv2.cvtColor(rasm, cv2.COLOR_BGR2RGB)
    yuzlar = []
    for y in kordinatalar:
        x1 = int(y["bbox"][0])
        y1 = int(y["bbox"][1])
        x2 = int(y["bbox"][2])
        y2 = int(y["bbox"][3])
        yuz_i = rasm[y1:y2, x1:x2]
        yuz_i = cv2.resize(yuz_i, (112, 112))
        yuzlar.append(yuz_i)
    embeddinglar = []
    for _, (yuz_i, koord_i) in enumerate(zip(yuzlar, kordinatalar)):
        embedding = model.get(rasm, koord_i)
        embeddinglar.append([embedding, yuz_i])
    return embeddinglar

def piksel_olish(rasm, kordinatalar):
    """
    Berilgan rasmdan kordinatalar bo'yicha yuz rasmini qirqib,
    undan pilsellarni olib listga o'tkazamiz

    Parameters
    ----------
    rasm : numpy
    kordinatalar : list

    Returns
    -------
    list
        kordinatalar bo'yicha barcha yuzga tegishli piksellar
    """
    rasm = cv2.cvtColor(rasm, cv2.COLOR_BGR2RGB)
    piksellar = []
    for kord in kordinatalar:
        x1 = int(kord["bbox"][0])
        y1 = int(kord["bbox"][1])
        x2 = int(kord["bbox"][2])
        y2 = int(kord["bbox"][3])
        yuz_i = rasm[y1:y2, x1:x2]
        yuz_i = cv2.resize(yuz_i, (112, 112))
        # matrixdan vectorga o'tdik
        piksellar_i = yuz_i.reshape((1, 3*112*112))
        piksellar.append([piksellar_i.tolist()[0], yuz_i])
    return piksellar

def rasm_kursat(rasm, sarlavha=""):
    cv2.imshow(sarlavha, rasm)
    cv2.waitKey()

def rasm_olish(joy=""):
    return cv2.imread(joy)  # [0, 255]
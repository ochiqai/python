import face_recognition as fr  # ramsdagi yuzlar bilan ishlash uchun
import cv2  # ramslar bilan ishlash uchun
import gradio as gr  # web app qilish uchun


def qayta_ulchamlash(image, balandlik=500):
    """
    rasmni berilgan balandlik buyicha o'lchami o'zgartirish
    :param image: rasm
    :param balandlik:
    :return: o'lchami o'zgartirilgan rasm
    """

    # proporsiya (mutanosiblik) hisoblanishi
    proporsiya = float(image.shape[1])/float(image.shape[0])

    # balnlikka mos, enining hisoblanishi
    eni = int(balandlik/proporsiya)

    # rasmning o'lchami o'zgartirilishi
    resized_image = cv2.resize(image, (balandlik, eni))
    return resized_image


def yuz_qirq(rasm):
    """
    Bu funksiya berilgan rasmni olib, burun kordinatasi joylashgan joyni topib, o'sha bo'yicha
    yuzni qirqadi.
    :param rasm:
    :return: qirqilgan rasmni qaytaradi, uning o'lchami 600x600 bo'ladi.
    """

    # Agar rams o'lchami 600x600 (balandlik x eni) dan kichik bo'lsa, uni qayta o'lchamlaymiz
    if (rasm.shape[0] < 600 or rasm.shape[1] < 600):
        rasm = qayta_ulchamlash(rasm, balandlik=1200)

    # rasmdan burunnni aniqlab olish
    yuz_nuqtalar_list = fr.face_landmarks(rasm)
    burun_koordinatalari = yuz_nuqtalar_list[0]["nose_tip"]

    # berilgan burun koordinatalardan markazni topish, kordinatalar o'rta arifmetigi
    y_markaz, x_markaz = 0, 0
    for y, x in burun_koordinatalari:
        y_markaz += y
        x_markaz += x
    y_markaz = y_markaz // len(burun_koordinatalari)
    x_markaz = x_markaz // len(burun_koordinatalari)

    # yuqorida aniqlangan (x_markaz, y_markaz) kordinatalari bo'yicha ramsni qirqamiz.
    # rasm 600x600 bo'lishi uchun, x koordinatasi bo'yicha
    #   x_markaz - 400 nuqtadan x_markaz + 200 nuqtagacha
    # y kordinatasi bo'yicha
    #   y_markaz - 300:y_markaz + 300
    qirqilgan_rasm = rasm[x_markaz - 400:x_markaz + 200, y_markaz - 300:y_markaz + 300, :]

    return qirqilgan_rasm

# gradioda programma qilib uni ishlatish
iface = gr.Interface(fn=yuz_qirq, inputs="image", outputs="image").launch()
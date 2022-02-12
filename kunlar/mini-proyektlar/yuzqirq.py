import matplotlib.pyplot as plt
import face_recognition as fr
import cv2
import gradio as gr



def resize(image, balandlik=500):
    aspect_ratio = float(image.shape[1])/float(image.shape[0])
    eni = balandlik/aspect_ratio
    image = cv2.resize(image, (int(balandlik),int(eni)))
    return image

def yuz_qirq(img):
    if (img.shape[0] < 600 or img.shape[1] < 600):
        img = resize(img, balandlik=1200)
    # rasmdan burunnni aniqlab olish
    yuz_nuqtalar_list = fr.face_landmarks(img)
    burun_koordinatalari = yuz_nuqtalar_list[0]["nose_tip"]

    # markazni topish
    y_markaz, x_markaz = 0, 0
    for y, x in burun_koordinatalari:
        y_markaz += y
        x_markaz += x
    y_markaz = y_markaz // len(burun_koordinatalari)
    x_markaz = x_markaz // len(burun_koordinatalari)
    # qirqilgan_rasm = img[x_markaz - 400:x_markaz + 200, y_markaz - 300:y_markaz + 300, :]

    qirqilgan_rasm = img[x_markaz-700:x_markaz+700, y_markaz-700:y_markaz+700,:]
    if (qirqilgan_rasm.shape[0] > 600 or qirqilgan_rasm.shape[1] > 600):
        qirqilgan_rasm = resize(qirqilgan_rasm,  balandlik=600)

    return qirqilgan_rasm

iface = gr.Interface(fn=yuz_qirq, inputs="image", outputs="image").launch()



# img = fr.load_image_file("./imgs/trump.jpg")
# print(img.shape)
#
# if (img.shape[0] < 600 or img.shape[1] < 600):
#     img = resize(img,  balandlik=1200)
#
# print(img.shape)
#
#
#
#
# print("Rasm o'lchami: ", img.shape)
# # plt.imshow
#
# # rasmdan burunnni aniqlab olish
# yuz_nuqtalar_list = fr.face_landmarks(img)
#
# # for nuqta, koord in yuz_nuqtalar_list[0].items():
# #     print(nuqta, koord)
#
# burun_koordinatalari = yuz_nuqtalar_list[0]["nose_tip"]
#
# # markazni topish
# print(burun_koordinatalari)
# y_markaz, x_markaz = 0, 0
# for y, x in burun_koordinatalari:
#     y_markaz += y
#     x_markaz += x
#
# y_markaz = y_markaz // len(burun_koordinatalari)
# x_markaz = x_markaz // len(burun_koordinatalari)
#
# # burun koord. chizish
# # cv2.rectangle(img, (y_markaz, x_markaz), (y_markaz+3, x_markaz+3), (0, 255, 255), 5)
# # plt.imshow(img)
# # plt.show()
#
#
# qirqilgan_rasm = img[x_markaz-400:x_markaz+200, y_markaz-300:y_markaz+300,:]
# # qirqilgan_rasm = img[x_markaz-700:x_markaz+700, y_markaz-700:y_markaz+700,:]
# # if (qirqilgan_rasm.shape[0] > 600 or qirqilgan_rasm.shape[1] > 600):
# #     qirqilgan_rasm = resize(qirqilgan_rasm,  balandlik=600)
# print("Qirqilgan rasm o'lchami: ", qirqilgan_rasm.shape)
# plt.imshow(qirqilgan_rasm)
# plt.show()
#
#
#
#
# # # # Display the results
# # # for (x, y) in burun_koordinatalari:
# #     # Draw a box around the face
# #     cv2.rectangle(img, (x, y), (x+30, y+30), (0, 0, 255), 2)
# #
# # # Display the resulting image
# # # cv2.imshow('Video', img)
# #
# # plt.imshow(img)
# # plt.show()
# # # Hit 'q' on the keyboard to quit!
# #
# #
# #
# #

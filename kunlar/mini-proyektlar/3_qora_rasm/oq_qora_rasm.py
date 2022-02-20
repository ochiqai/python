import matplotlib.pyplot as plt # rasmlar bilan ishlash uchun biblioteka
import gradio as gr # web app qilish uchun biblioteka


def oq_qora(rasm):
    """
    Ushbu funksiya berilgan rasmni oq-qara rasmga o'tkazadi. Bu ingliz tilida greyscale deb ataladi.
    :param rasm: (HxEx3) o'lchamli rasm, H - bu balandlik, E - bu eni.
    :return:
    """
    # berilgan rasmni piksellarini 0 va 1 oraliqda [0,1] qilib olish
    rasm = rasm / 255

    # rasmning qizil (R-red), yashil (G-green) va ko'k (B-blue) qismini olayapmiz
    R, G, B = rasm[:, :, 0], rasm[:, :, 1], rasm[:, :, 2]

    # R,G,B larni qorishtirayapmiz
    rasm_oq_qora = 0.2989 * R + 0.5870 * G + 0.1140 * B
    return rasm_oq_qora


# terminalda ishlatish
img = plt.imread('trump.jpg')/255
_oq_qora = oq_qora(img)
plt.imshow(_oq_qora, cmap='gray')
plt.show()

# gradio da ishlatish
# ginter = gr.Interface(fn=oq_qora, inputs="image", outputs="image")
# ginter.launch()

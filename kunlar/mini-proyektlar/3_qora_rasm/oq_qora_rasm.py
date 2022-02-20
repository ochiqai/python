import matplotlib.pyplot as plt
import gradio as gr


def oq_qora(img):
    img = img / 255
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    img_oq_qora = 0.2989 * R + 0.5870 * G + 0.1140 * B
    return img_oq_qora

# img = plt.imread('green.jpg')/255
# _oq_qora = oq_qora(img)
# plt.imshow(_oq_qora, cmap='gray')
# plt.show()

ginter = gr.Interface(fn=oq_qora, inputs="image", outputs="image")
ginter.launch()

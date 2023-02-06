import cv2
# import gradio as gr


from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash
)

video_joy = "/home/nuriddin/ochiqai/python/projects/gradio_apps/video/video.mp4"
cap = cv2.VideoCapture(video_joy)
_, rasm = cap.read()
# rasm: <class 'numpy.ndarray'>
# len(rasm) = 1280

aniqlagich_model = model_yuklash(turi="aniqlagich")
embedding_model = model_yuklash(turi="embedding")
kordinatalar = aniqlash(aniqlagich_model, rasm)
embedding = embedding_model.get(rasm, kordinatalar) #embedding: <class 'numpy.ndarray'>, len(embedding):512


i = 0
fayl_och = open("embeddinglar.txt", "w")
while i < len(embedding):
    embedding_str = str(embedding[i])
    fayl_och.write(embedding_str)
    fayl_och.write(" ")
    i = i + 1


# file_open = open("embeddinglar.txt", "r")
# tekst = file_open.readlines()
# print(tekst)


# def kamera(cap):
#
#     return embedding
#
#
# demo = gr.Interface(
#     kamera,
#     gr.Image(source="webcam", streaming=True),
#     "text",
#     live=True
# )
#
# demo.launch()



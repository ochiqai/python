import gradio as gr

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, chizish
)

#------------- Dastur haqida ----------------------
#  Kamera orqali kiradigan rasmdan, yuz qismini aniqlash.
#--------------------------------------------------

#------------- Algoritm ---------------------------
#   -Kirish:
#       Rasmlarni kameradan olamiz.
#   -Rasmdan yuz qismini aniqlash:
#        1. Kerakli modulni yuklab olamiz. (detection)
#        2. Rasm kordinatasini aniqlab olamiz.
#   -Chiqish:
#       Chizilgan rasm (yuz qismi aniqlanadi va unga turtburchak chiziq chiziladi)
#--------------------------------------------------

def kamera(rasm):
    """
    Kamera orqali kiritilgan rasmning yuz qismini aniqlaydi.
    Parameters
    ----------
    rasm: <class 'numpy.ndarray'>
        kamera orqali kiradigan rasm
    Returns
    -------
    rasm : <class 'numpy.ndarray'>
        rasm_chizilgan (yuz qismiga turburchak chiziq chizilgan rasm)
    """
    # detection modul yuklash
    aniqlagich_model = model_yuklash(turi="aniqlagich")
    # rasm kordinnatasini olish
    kordinatalar = aniqlash(
        model=aniqlagich_model,
        rasm=rasm
    )
    # yuz qismini chizib olish
    rasm_chizilgan = chizish(
        rasm=rasm,
        kordinatalar=kordinatalar
    )
    return rasm_chizilgan


demo = gr.Interface(
    kamera,
    gr.Image(source="webcam", streaming=True),
    "image",
    live=True
)

demo.launch()


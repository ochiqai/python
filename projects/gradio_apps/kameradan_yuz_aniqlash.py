import gradio as gr

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, chizish
)

def kamera(rasm):
    # rasm: class 'numpy.ndarray'
    aniqlagich_model = model_yuklash(turi="aniqlagich")
    kordinatalar = aniqlash(
        model=aniqlagich_model,
        rasm=rasm
    )
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
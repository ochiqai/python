import gradio as gr


from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, chizish
)

#------------- Dastur haqida ----------------------
#  Kameradan yuz qismini aniqlash
#--------------------------------------------------

#------------- Algoritm ---------------------------
#   1. Kerakli modullarni yuklash. (detection)
#   2. Kordinata aniqlanadi.
#   3. rasm_chizilgan funksiyasini yuklash.
#--------------------------------------------------



def kamera(rasm):
    """
    Kamera orqali kiritilgan rasmni yuz qismini aniqlaydi.
    Parameters
    ----------
    rasm: numpy

    Returns
    -------
    rasm : numoy
        chizilgan rasm
    """
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
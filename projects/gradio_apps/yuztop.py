import gradio as gr

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, chizish
)


def yuz_aniqlagich(rasm):
    aniqlagich_model = model_yuklash(turi="aniqlagich")
    kordinatalar = aniqlash(
        model=aniqlagich_model,
        rasm=rasm
    )
    rasm_chizilgan = chizish(
        rasm=rasm,
        kordinatalar=kordinatalar
    )
    return rasm_chizilgan, "Yuzlar aniqlandi va ular {} ta".format(len(kordinatalar))


with gr.Blocks() as demo:
    name = gr.Image(label="Rasm")
    output_rasm = gr.Image(label="Yuzlar aniqlangan rasm")
    output_text = gr.Textbox(label="Malumot")
    tugma = gr.Button("Bosing")
    tugma.click(fn=yuz_aniqlagich, inputs=name, outputs=[output_rasm, output_text])

demo.launch(share=True)

import gradio as gr
from aura_sr import AuraSR
from PIL import Image

aura_sr = AuraSR.from_pretrained()


def image_echo(img: Image):
    img4x = aura_sr.upscale_4x_overlapped(img)
    return img4x


iface = gr.Interface(
    fn=image_echo,
    inputs=gr.Image(type="pil", label="Input Image"),
    outputs=gr.Image(type="pil", label="Output Image", format="jpg"),
    title="SR",
    description="Upload an image.",
)

iface.launch(share=True)

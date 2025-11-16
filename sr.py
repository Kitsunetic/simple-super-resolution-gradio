import argparse

import gradio as gr
from aura_sr import AuraSR
from PIL import Image

P = argparse.ArgumentParser()
P.add_argument("--public", action="store_true", help="Open public URL")
P.add_argument("--format", default="jpg", help="Output image format")
P.add_argument(
    "--batch_size",
    type=int,
    default=8,
    help="Batch size for the windows. Large batch size accelerates but requires large memory",
)
P.add_argument(
    "--non-overlap",
    action="store_true",
    help="Non-overlap super resolution. Accelerates a little bit but reduces quality",
)
args = P.parse_args()

aura_sr = AuraSR.from_pretrained()


def image_echo(img: Image):
    if args.non_overlap:
        img4x = aura_sr.upscale_4x(img, max_batch_size=args.batch_size)
    else:
        img4x = aura_sr.upscale_4x_overlapped(img, max_batch_size=args.batch_size)
    return img4x


iface = gr.Interface(
    fn=image_echo,
    inputs=gr.Image(type="pil", label="Input Image"),
    outputs=gr.Image(type="pil", label="Output Image", format=args.format),
    title="SR",
    description="Upload an image.",
)

iface.launch(share=args.public)

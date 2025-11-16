from setuptools import find_packages, setup

setup(
    name="gradio-sr-app",
    version="0.0.1",
    packages=find_packages(),
    py_modules=["sr"],
    install_requires=[
        "torch",
        "torchvision",
        "Pillow",
        "transformers",
        "gradio",
        "diffusers",
        "aura-sr",
    ],
    entry_points={
        "console_scripts": [
            "sr = sr:iface.launch",
        ],
    },
    author="Kitsunetic",
    description="A Gradio app for Aura Super-Resolution.",
)

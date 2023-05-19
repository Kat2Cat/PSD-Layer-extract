from psd_tools import PSDImage
from pathlib import Path
import os

src = input("Folder Location: ")
dirpath = Path(src)

Counter = 1
def extract_layers(psd):
    global Counter
    for layer in psd:
        if layer.name == '背景':
            layer_image = layer.composite()
            layer_image.save(str(Counter)+'.png')
            Counter += 1


for file in dirpath.glob("**/*"):
    file_path = os.path.join(src, file)
    if os.path.isfile(file_path) :
        psd = PSDImage.open(file_path)
        extract_layers(psd)


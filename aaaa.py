from PIL import Image
import os
import sys
from PIL import Image
import pyocr
tesseract_path = "C:\Program Files\Tesseract-OCR"
if tesseract_path not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + tesseract_path

    tools = pyocr.get_available_tools() 
if len(tools) == 0:
    print("OCRエンジンが指定されていません")
    sys.exit(1)
else:
    tool = tools[0]

    

#　画像の読み込み
img = Image.open('OIP.jpg')

builder = pyocr.builders.TextBuilder(tesseract_layout=6)
result = tool.image_to_string(img,lang="jpn",builder=builder)
print(result)
# 画像の表示
img.show()

from PIL import Image
#pipが使えない場合システム環境変数から直接pip.exeのファイルを追加するC:\Users\Administrator\AppData\Local\Programs\Python\Python312\Scripts

#　画像の読み込み 
img = Image.open('Eチーム制作物フローチャート.drawio.png')

img.show()
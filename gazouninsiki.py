#pip install Pillow
#pip install pyocr
#↑これをターミナルで実行



from PIL import Image
import tkinter
import tkinter.filedialog
import os
import sys
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

### 定数
WIDTH  = 640        # 幅
HEIGHT = 400        # 高さ
 
### 関数
def func():
    ### ファイルダイアログ
    name = tkinter.filedialog.askopenfilename(title="ファイル選択", initialdir="C:/", filetypes=[("Image File","*.png")])
 
    ### 画像ロード
    image = Image.open(name)
 
    ### キャンバスに表示
    canvas.create_image(WIDTH/2, HEIGHT/2, image=tkinter.PhotoImage(image))
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    result = tool.image_to_string(image, lang="jpn", builder=builder)
    print(result)

### メイン画面作成
main = tkinter.Tk()

### 画面サイズ設定
main.geometry("640x440")

### ボタン作成・配置
button = tkinter.Button(main, text="ファイル選択", command=func)
button.pack()

### キャンバス作成・配置
canvas = tkinter.Canvas(main, width=WIDTH, height=HEIGHT)
canvas.pack()

### イベントループ
main.mainloop()
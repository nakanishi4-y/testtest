from PIL import Image, ImageTk
import tkinter
import tkinter.filedialog
import os
import sys
import pyocr

tesseract_path = r"C:\Program Files\Tesseract-OCR"  # バックスラッシュをエスケープする
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
TEXT_WIDTH = 320    # テキスト表示領域の幅

### 関数
def func():
    ### ファイルダイアログ
    name = tkinter.filedialog.askopenfilename(title="ファイル選択", initialdir="C:/", filetypes=[("Image File","*.png")])
 
    ### 画像ロード
    global image_tk  # グローバル変数として画像を保持
    image = Image.open(name)
 
    ### 文字抽出
    lang = lang_var.get()  # 選択された言語を取得
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    result = tool.image_to_string(image, lang=lang, builder=builder)
    
    ### キャンバスに画像を表示
    image.thumbnail((TEXT_WIDTH, HEIGHT), Image.BICUBIC)  # BICUBICを使用
    image_tk = ImageTk.PhotoImage(image)
    canvas.delete("all")  # キャンバス内のすべての要素を削除
    canvas.create_image(TEXT_WIDTH/2, HEIGHT/2, image=image_tk)
    
    ### キャンバスに文字を表示
    canvas.create_text(TEXT_WIDTH + (WIDTH - TEXT_WIDTH)/2, HEIGHT/2, text=result, font=("Helvetica", 12), anchor="w")

### メイン画面作成
main = tkinter.Tk()

### 画面サイズ設定
main.geometry("960x440")

### ラジオボタン用の変数
lang_var = tkinter.StringVar(value="jpn")  # 初期値を日本語に設定

### ファイル選択ボタン作成・配置
button = tkinter.Button(main, text="ファイル選択", command=func)
button.pack(side="left")

### ラジオボタン作成・配置（日本語）
jpn_radio = tkinter.Radiobutton(main, text="日本語", variable=lang_var, value="jpn")
jpn_radio.pack(side="left")

### ラジオボタン作成・配置（英語）
eng_radio = tkinter.Radiobutton(main, text="English", variable=lang_var, value="eng")
eng_radio.pack(side="left")

### キャンバス作成・配置
canvas = tkinter.Canvas(main, width=WIDTH, height=HEIGHT)
canvas.pack()

### イベントループ
main.mainloop()
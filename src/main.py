# Import
import tkinter as tk
import tkinter.filedialog as filedialog
from unittest import self
from tkinter import messagebox
import chardet

# ここからプログラム,meta系
root = tk.Tk()
root.title(u"Ik NotePad")
root.geometry("400x300")

# メインのテキストボックス
textbox = tk.Text(root,bg="white",fg="black",height=80)
textbox.pack()

# テキストボックスの大きさを可変にする
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# 保存
root.bind('<Control-KeyPress-s>', save_file_as)
def save_file_as(event=None):
    """名前を付けて保存する"""
    f_type = [('Text', '*.txt')]

    file_path = root.filedialog.asksaveasfilename(
        filetypes=f_type)

    if file_path != "":
        with open(file_path, "w") as f:
            f.write(text_widget.get("1.0", "end-1c"))

return


#メニューバーの設定(ファイル)
menubar = tk.Menu(self.root)                                  
FileMenu = tk.Menu(tearoff=0)
FileMenu.add_command(label="新規(Ctrl+N)",command=self.new)
FileMenu.add_command(label="開く(Ctrl+O)",command=self.onOpen)
FileMenu.add_command(label="名前を付けて保存(Alt+S)",command=self.onSave)
FileMenu.add_command(label="保存(Ctrl+S)",command=self.onSaves)
FileMenu.add_separator()
FileMenu.add_command(label="終了",command=self.root.quit)

#メニューバーの設定(編集)
helpmenu = tk.Menu(menubar, tearoff=0,)
helpmenu.add_command(label='検索する(ファイル開くと使用可能)(Ctrl+F)', command=self.sub_window)
helpmenu.add_command(label='全て選択(Ctrl+A)', command=self.selct_all)
helpmenu.add_command(label='コピー(Ctrl+C)', command=self.copy)
helpmenu.add_command(label='貼り付け(Ctrl+V)', command=self.paste)
helpmenu.add_command(label='切り取り(Ctrl+X)', command=self.cut)

#開く
def onOpen(self):
dialog = filedialog.askopenfilename(filetypes=[("All Files","*.*")])
if len(dialog) != 0:
 
#文字コードを自動識別して読み取るコード
FILENAME = dialog 
            
self.filename = FILENAME
tmp = open(FILENAME,"rb")
encode = chardet.detect(tmp.read())["encoding"]
file = open(FILENAME,"r",encoding=encode,errors="ignore") 
text = file.read()
file.close()
print(dialog)

#一度文字を全て削除してから挿入する
self.textbox.delete("1.0",tk.END)
self.textbox.insert("1.0",text)
self.text2 = self.textbox.get("1.0","end")

#保存
def onSave(self):
dialog = filedialog.asksaveasfilename(filetypes=[("All Files","*.*")])
defaultextension = "txt"
if len(dialog) != 0:
file = open(dialog,"w",encoding="UTF-8",errors="ignore")
file.write(self.textbox.get("1.0",tk.END))
self.text2 = self.textbox.get("1.0","end")
self.none = self.textbox.get("1.0","end")
file.close()

#ここまでプログラム
root.mainloop()
# Import
import sys
import tkinter

# ここからプログラム,meta系
root = tkinter.Tk()
root.title(u"Ik NotePad")
root.geometry("400x300")

# メインのテキストボックス
textbox = tkinter.Text(root,bg="white",fg="black",height=80)
textbox.pack()

# テキストボックスの大きさを可変にする
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# 保存
def save_file_as(event=None):
    """名前を付けて保存する"""
    f_type = [('Text', '*.txt')]

    file_path = tkinter.filedialog.asksaveasfilename(
        filetypes=f_type)

    if file_path != "":
        with open(file_path, "w") as f:
            f.write(text_widget.get("1.0", "end-1c"))

    return

root.bind('<Control-KeyPress-s>', save_file_as)

# ここまでプログラム
root.mainloop()
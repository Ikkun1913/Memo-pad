import tkinter

root = tkinter.Tk()
root.title(u"Ik NotePad")
root.geometry("400x300")
# ここからプログラム
textbox = tkinter.Text(root,bg="white",fg="black",height=80)
textbox.pack()

root.mainloop()
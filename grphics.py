from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk


class MyWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        btn1 = Button(text="Выбрать картинку", background="green", foreground="black",
                      padx="200", pady="7", font="13", command=self.open_img)
        btn1.place(x=50, y=20)
        btn2 = Button(text="Нанести водяной знак", background="green", foreground="black",
                      padx="200", pady="7", font="13")
        btn2.place(x=760, y=20)

    def open_img(self):
        path = filedialog.askopenfilename(title='open')
        if path:
            img = ImageTk.PhotoImage(Image.open(path).resize((750, 400)))
            panel = Label(image=img)
            panel.image = img
            panel.place(x=660, y=150)
        else:
            print('Картинка не выбрана')


root = Tk()
root.geometry("1500x600")
root.resizable(width=False, height=False)
root.title("Watermarking an image")
MyWindow(root).pack()
root.mainloop()

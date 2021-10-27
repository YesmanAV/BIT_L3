from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk


class MyWindow:

    def __init__(self, **kw):
        super().__init__(**kw)
        btn1 = Button(text="Выбрать картинку", background="green", foreground="black",
                      padx="200", pady="7", font="13", command=self.open_img)
        btn1.place(x=50, y=20)
        btn2 = Button(text="Нанести водяной знак", background="green", foreground="black",
                      padx="200", pady="7", font="13")
        btn2.place(x=760, y=20)
        self.box = Listbox(width=90, height=30)
        self.box.place(x=50, y=100)

    def open_img(self):
        try:
            path = filedialog.askopenfilename(title='open')
            if path:
                img = ImageTk.PhotoImage(Image.open(path).resize((750, 400)))
                panel = Label(image=img)
                panel.image = img
                panel.place(x=670, y=100)
            else:
                self.box.insert(END, 'ERROR:    Картинка не выбрана')
                print('Картинка не выбрана')
        except Exception as ex:
            self.box.insert(END, 'ERROR:' + str(ex))



root = Tk()
root.geometry("1500x600")
root.resizable(width=False, height=False)
root.title("Watermarking an image")
MyWindow()
root.mainloop()

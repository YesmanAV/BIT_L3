from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk


def display(im):
    img = im.resize((750, 400))
    panel = Label(image=img)
    panel.image = img
    panel.place(x=670, y=100)


class MyWindow:

    def __init__(self, **kw):
        super().__init__(**kw)
        self.panel = Label()
        self.img = None
        self.btn1 = Button(text="Выбрать картинку", background="grey", foreground="black",
                      padx="200", pady="7", font="13", command=self.open_img)
        self.btn1.place(x=50, y=20)
        self.btn2 = Button(text="Нанести водяной знак", background="grey", foreground="black",
                      padx="186", pady="7", font="13")
        self.btn2.place(x=50, y=80)
        self.box = Listbox(width=90, height=20)
        self.box.place(x=50, y=150)
        self.path1 = ''

    def open_img(self):
        if self.path1 != '':
            self.clear_label_image()
        self.box.delete(0, END)
        try:
            path = filedialog.askopenfilename(title='Открыть')
            if path:
                self.path1 = path
                self.img = ImageTk.PhotoImage(Image.open(path).resize((610, 400)))
                self.panel = Label(image=self.img)
                self.panel.image = self.img
                self.panel.place(x=650, y=40)
            else:
                self.box.insert(END, 'ERROR:    Картинка не выбрана')
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))

    def clear_label_image(self):
        self.panel.destroy()

    def send_image(self):
        print('Code')


root = Tk()
root.geometry("1300x500")
root.resizable(width=False, height=False)
root.title("Watermarking an image")
MyWindow()
root.mainloop()

from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk


class MyWindow:

    def __init__(self, **kw):
        super().__init__(**kw)
        self.panel = Label()
        self.btn1 = Button(text="Выбрать картинку", background="grey", foreground="black",
                           padx="200", pady="7", font="13", command=self.open_img)
        self.btn1.place(x=50, y=20)
        self.btn2 = Button(text="Нанести водяной знак", background="grey", foreground="black",
                           padx="186", pady="7", font="13", command=self.send_image)
        self.btn2.place(x=50, y=80)
        self.box = Listbox(width=90, height=20)
        self.box.place(x=50, y=150)
        self.send_path = ''

    def open_img(self):
        try:
            if self.send_path != '':
                self.clear_label_image()
            self.box.delete(0, END)
            path = filedialog.askopenfilename(title='Открыть')
            if path:
                self.send_path = path
                img = ImageTk.PhotoImage(Image.open(path).resize((650, 400)))
                self.panel = Label(image=img)
                self.panel.image = img
                self.panel.place(x=620, y=40)
            else:
                self.send_path = ''
                self.box.insert(END, 'ERROR:    Картинка не выбрана')
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))

    def clear_label_image(self):
        self.panel.destroy()

    def display(self, image):
        try:
            self.clear_label_image()
            img = image.resize((650, 400))
            self.panel = Label(image=img)
            self.panel.image = img
            self.panel.place(x=620, y=40)
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))

    def send_image(self):
        try:
            if self.send_path != '':
                self.box.insert(END, '###   Картинка отправлена    ###')
                # Код
            else:
                self.box.insert(END, 'ERROR:    Картинка не выбрана')
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))


root = Tk()
root.geometry("1300x500")
root.resizable(width=False, height=False)
root.title("Watermarking an image")
MyWindow()
root.mainloop()

from PIL import Image

def resize_img(file):
    img = Image.open(file)
    width, height = img.size
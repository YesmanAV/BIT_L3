from PIL import Image

def resize_img(file):
    img = Image.open(file)
    width, height = img.size
    white_width = 0
    white_height = 0
    while (white_width < width or white_height < height):
        white_height += 9
        white_width += 16
        
    white_img = Image.new('RGB', (white_width, white_height), 'white')
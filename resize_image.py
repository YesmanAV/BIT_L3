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

    x = int((white_img.size[0] - width) / 2)
    y = int((white_img.size[1] - height) / 2)

    white_img.paste(img, (x, y))
    return white_img
# 
# if __name__ == '__main__':
#     imgage = resize_img('depositphotos_107694484-stock-photo-little-boy.jpg')
#     imgage.save("resized_img.jpg")
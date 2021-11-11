from PIL import Image
from save_instruments import save_edited_image
from save_instruments import add_to_edited_table

def watermark_photo(input_image_path, watermark_image_path, output_name, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))

    if base_image.size > watermark.size:
        transparent.paste(watermark, position, mask=watermark)
        save_edited_image(transparent.convert('RGB'), output_name)
        add_to_edited_table(output_name)
        print('The watermark was successfully applied to the picture')
    else:
        print('Error!!! The size of the watermark is larger than the original photo!')

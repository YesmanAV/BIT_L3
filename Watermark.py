from PIL import Image

def watermark_photo(input_image_path, watermark_image_path, output_image_path, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    base_image.paste(watermark, position)
    base_image.show()
    base_image.save(output_image_path)
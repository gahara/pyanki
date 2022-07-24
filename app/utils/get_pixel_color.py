from PIL import Image


def get_pixel_color(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    r, g, b = pixels[10, 10]
    hex_color_code = f'#{r:02x}{g:02x}{b:02x}'
    return hex_color_code, img


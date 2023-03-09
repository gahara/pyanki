import os
import random
from flask import render_template
from app import app
from app.utils.reader import read_file_names
from app.utils.get_pixel_color import get_pixel_color

KANJI = 'kanji'
IMAGES_PATH = os.path.join(app.static_folder, KANJI)
IMAGES_NAMES = read_file_names(IMAGES_PATH)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'


@app.route('/random_kanji')
def show_kanji():
    random_kanji_image = random.choice(IMAGES_NAMES)
    image_hex_color, img = get_pixel_color(f'{IMAGES_PATH}/{random_kanji_image}')
    width, height = img.size
    message = 'next kanji is: '
    path_to_image = f'/static/kanji/{random_kanji_image}'
    return render_template(
        'random_kanji.html',
        message=message,
        kanji=path_to_image,
        veil=image_hex_color,
        img_width=width,
        img_height=height
    )

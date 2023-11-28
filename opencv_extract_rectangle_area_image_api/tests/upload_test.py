from pathlib import Path

from requests import post

BASE_DIR = Path(__file__).resolve().parent


def test_upload_with_red_rectangle_image():
    url = 'http://localhost:8000'
    image = f'{BASE_DIR}/assets/example_image_with_red_rectangle.png'

    with open(image, 'rb') as image_file:
        response = post(f'{url}/extract', files={
            "file": image_file
        }, timeout=60)

    json = response.json()
    assert json['x'] == 85
    assert json['y'] == 16
    assert json['h'] == 165
    assert json['w'] == 140

def test_upload_without_red_rectangle_image():
    url = 'http://localhost:8000'
    image = f'{BASE_DIR}/assets/example_image_without_red_rectangle.png'

    with open(image, 'rb') as image_file:
        response = post(f'{url}/extract', files={
            "file": image_file
        }, timeout=60)

    json = response.json()
    assert json == {'msg': 'Error to extract the rectangle'}

def test_upload_with_multiples_rectangles_image():
    url = 'http://localhost:8000'
    image = f'{BASE_DIR}/assets/example_image_multiples_rectangles.png'

    with open(image, 'rb') as image_file:
        response = post(f'{url}/extract', files={
            "file": image_file
        }, timeout=60)

    json = response.json()
    assert json['x'] == 288
    assert json['y'] == 298
    assert json['h'] == 100
    assert json['w'] == 272

def test_upload_invalid_image():
    url = 'http://localhost:8000'
    image = f'{BASE_DIR}/assets/example_image_invalid_format.jpeg'

    with open(image, 'rb') as image_file:
        response = post(f'{url}/extract', files={
            "file": image_file
        }, timeout=60)
    
    json = response.json()
    assert json == {'msg': 'Image not valid'}

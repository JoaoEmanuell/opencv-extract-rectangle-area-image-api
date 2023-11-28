from uuid import uuid4
from os.path import splitext, exists
from os import mkdir, remove
from pathlib import Path

from flask import Flask, request, jsonify

from src import extract_red_rectangle

BASE_DIR = Path(__file__).resolve().parent
TMP_PATH = f'{BASE_DIR}/tmp'
VALID_FILE_EXTENSIONS = ('.png', '.jpg')

# create dirs

if not exists(TMP_PATH):
    mkdir(TMP_PATH)

app = Flask(__file__)

@app.route('/extract', methods=["POST"])
def extract():
    if request.method == 'POST':
        file = request.files["file"]

        _, file_extension = splitext(file.filename) # get the file_extension, ignore the filename

        # validate the file_extension
        if file_extension not in VALID_FILE_EXTENSIONS:
            return jsonify({'msg': 'Image not valid'}), 400

        filename = f'{TMP_PATH}/{uuid4()}{file_extension}' # generate a filename with full path to save

        file.save(filename) # save the file

        # start the extract

        try:
            extract_red = extract_red_rectangle(filename)
            remove(filename)
            return jsonify(extract_red), 200
        except Exception as err:
            print(err)
            remove(filename)
            return jsonify({'msg': 'Error to extract the rectangle'}), 400
    else:
        return jsonify({'msg': 'Method not allowed'}), 405
    
if __name__ == '__main__':
    app.run('0.0.0.0', 8000, False)
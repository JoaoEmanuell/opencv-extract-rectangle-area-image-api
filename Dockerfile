FROM hdgigante/python-opencv:4.8.1-alpine

RUN pip install --upgrade pip

WORKDIR /usr/src/app

# Install

COPY opencv_extract_rectangle_area_image_api .

RUN pip install -r requirements.txt

# Ports and run

EXPOSE 8000

CMD ["python", "app.py"]
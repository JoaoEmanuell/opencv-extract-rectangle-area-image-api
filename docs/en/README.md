# Extract

The red rectangle must be between the colors #FF0000 [RGB(255, 000, 000)] and #F00000 [RGB(240, 000, 000)], otherwise the extraction will fail.

To extract the red rectangle from the image, access the */extract* route using the **POST** method.

Upload the image and wait for the response.

Example:

    url = 'endpoint'
    image = f'{BASE_DIR}/assets/example_image_with_red_rectangle.png'

Open the image:

    with open(image, 'rb') as image_file:

Send image to route, using the *files* and configure the expiration time in 60 seconds.

    response = post(f'{url}/extract', files={
        "file": image_file
    }, timeout=60)

After that convert the response to json.

    json = response.json()

It will contain the coordinates of the largest red rectangle in the image.

    {
        'x': 85, 
        'y': 16, 
        'h': 165,
        'w': 140
    }

## Rectangle not found

Case the rectangle not found, the returns will be as follows:

    {
        'msg': 'Error to extract the rectangle'
    }

## Invalid image

Case the image is invalid, the returns will be as follows:

    {
        'msg': 'Image not valid'
    }
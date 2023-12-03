import cv2
import numpy as np


def extract_red_rectangle(image_path: str) -> dict[str, int]:
    image = cv2.imread(image_path)  # read the image
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # set the rgb

    # set the range color

    red_range_init = np.array([200, 0, 0], dtype=np.uint8)
    red_range_end = np.array([255, 0, 0], dtype=np.uint8)

    mask = cv2.inRange(image_rgb, red_range_init, red_range_end)  # set the mask

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )  # get contours

    if contours:
        max_contour = max(contours, key=cv2.contourArea)  # get the bigger contour
        x, y, w, h = cv2.boundingRect(max_contour)  # positions
        return {"x": x, "y": y, "w": w, "h": h}  # return

    else:  # if not exists
        raise Exception("Red rectangle not found")

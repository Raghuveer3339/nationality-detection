import cv2
import numpy as np

def detect_dress_color(image):
    # Resize for faster processing
    image = cv2.resize(image, (200, 200))

    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Color ranges
    colors = {
        "red": [(0, 120, 70), (10, 255, 255)],
        "blue": [(100, 150, 0), (140, 255, 255)],
        "green": [(40, 40, 40), (80, 255, 255)],
        "white": [(0, 0, 200), (180, 30, 255)],
        "black": [(0, 0, 0), (180, 255, 50)],
        "yellow": [(20, 100, 100), (30, 255, 255)]
    }

    max_pixels = 0
    detected_color = "unknown"

    for color, (lower, upper) in colors.items():
        lower = np.array(lower)
        upper = np.array(upper)

        mask = cv2.inRange(hsv, lower, upper)
        pixels = cv2.countNonZero(mask)

        if pixels > max_pixels:
            max_pixels = pixels
            detected_color = color

    return detected_color
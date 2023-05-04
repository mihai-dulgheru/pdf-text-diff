import os

import cv2
import numpy as np
import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes

from constants import PATH, POPPLER_PATH
from functions.deskew import deskew


def box_boundaries(filename, page_num=1, level=2):
    """
    Draw boxes around the text on the specified page of a PDF file at the specified level of detail
    :param filename: The name of the PDF file
    :param page_num: The page number of the PDF file
    :param level: The level of detail to extract the boxes. An integer between 1 and 5.
                  1 -> page
                  2 -> block
                  3 -> paragraph
                  4 -> line
                  5 -> word
    :return: None
    """
    pdf_file = convert_from_bytes(open(os.path.join(PATH, filename), 'rb').read(), poppler_path=POPPLER_PATH)
    page_arr = np.asarray(pdf_file[page_num - 1])
    page_arr_gray = cv2.cvtColor(page_arr, cv2.COLOR_BGR2GRAY)
    page_arr_gray = cv2.fastNlMeansDenoising(page_arr_gray, None, 3, 7, 21)
    page_deskew = deskew(page_arr_gray)
    d = pytesseract.image_to_data(page_deskew, output_type=pytesseract.Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if d['level'][i] == level:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            # Draw green lines on boxes
            img = cv2.rectangle(page_arr, (x, y), (x + w, y + h), (0, 255, 0), 2)
    img_pil = Image.fromarray(img)
    img_pil.show()

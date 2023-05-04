import os

import cv2
import numpy as np
import pandas as pd
import pytesseract
from pdf2image import convert_from_bytes

from constants import PATH, POPPLER_PATH
from functions.combine_texts import combine_texts
from functions.confidence_value import confidence_value
from functions.deskew import deskew


def extract_text_from_pdfs(file_list, remove_header=False, remove_footer=False):
    """
    Extract text from a list of pdf files, returns a dictionary with the filename as key
and the extracted text and confidence values as value
    :param file_list: List of file names
    :param remove_header: If True, removes the header from each page
    :param remove_footer: If True, removes the footer from each page
    :return: A dictionary with the filename as key and the extracted text and confidence values as value
    """
    # Dictionary for saving dataframe of each pdf, where the filename is the key
    ocr_dic = {}
    for file in file_list:
        # Convert pdf into image
        pdf_file = convert_from_bytes(open(os.path.join(PATH, file), 'rb').read(), poppler_path=POPPLER_PATH)
        # Create a dataframe to save each pdf's text
        pages_df = pd.DataFrame(columns=['conf', 'text'])
        for (i, page) in enumerate(pdf_file):
            try:
                # Transfer image of pdf_file into array
                page_arr = np.asarray(page)
                # Transfer into grayscale
                page_arr_gray = cv2.cvtColor(page_arr, cv2.COLOR_BGR2GRAY)
                page_arr_gray = cv2.fastNlMeansDenoising(page_arr_gray, None, 3, 7, 21)
                page_deskew = deskew(page_arr_gray)
                # Calculate confidence value
                page_conf = confidence_value(page_deskew)
                # Extract string
                d = pytesseract.image_to_data(page_deskew, output_type=pytesseract.Output.DICT)
                d_df = pd.DataFrame.from_dict(d)
                # Drop header and footer by index
                if remove_header:
                    header_index = d_df[d_df['block_num'] == 1].index.values
                    d_df.drop(header_index, inplace=True)
                if remove_footer:
                    block_num = int(d_df.loc[d_df['level'] == 2, ['block_num']].max())
                    footer_index = d_df[d_df['block_num'] == block_num].index.values
                    d_df.drop(footer_index, inplace=True)
                # Combine text input dataframe
                text = combine_texts(d_df.loc[d_df['level'] == 5, 'text'].values)
                pages_df = pd.concat([pages_df, pd.DataFrame({'conf': [page_conf], 'text': [text]})],
                                     ignore_index=True)
            except Exception as e:
                if hasattr(e, 'message'):
                    pages_df = pd.concat([pages_df, pd.DataFrame({'conf': [-1], 'text': [e.message]})],
                                         ignore_index=True)
                else:
                    pages_df = pd.concat([pages_df, pd.DataFrame({'conf': [-1], 'text': [e]})], ignore_index=True)
                continue
        # Save dataframe into a dictionary with filename as key
        ocr_dic[file] = pages_df
        print('{} is done.'.format(file))

    return ocr_dic

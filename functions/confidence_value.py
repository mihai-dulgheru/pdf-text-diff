import pytesseract


def confidence_value(page_gray):
    """
    Return an average confidence value of OCR result
    :param page_gray: A grayscale image of a page
    :return: The average confidence value
    """
    df = pytesseract.image_to_data(page_gray, output_type='data.frame')
    df.drop(df[df.conf == -1].index.values, inplace=True)
    df.reset_index()

    return df.conf.mean()

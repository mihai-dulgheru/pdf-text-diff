def combine_texts(text_list, sep=' '):
    """
    Combine a list of texts into a single string
    :param text_list: List of strings to combine
    :param sep: Separator character to use between the texts (default is a space)
    :return: Combined text as a string
    """
    combined_text = sep.join(text_list)

    return combined_text

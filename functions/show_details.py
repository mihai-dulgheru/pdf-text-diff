import pandas as pd


def show_details(file_list, ocr_dic):
    """
    Displays details about OCR files and related text data
    :param file_list: List of file names
    :param ocr_dic: A dictionary containing two dataframes with text as a single column
    :return:
    """
    n = len(file_list)
    d = {'filename': [file_list[i] for i in range(n)],
         'conf': [ocr_dic[file_list[i]]['conf'].values[0] for i in range(n)],
         'text': [ocr_dic[file_list[i]]['text'].values[0] for i in range(n)]}
    df = pd.DataFrame(data=d, index=list(range(n)))
    pd.set_option('display.max_columns', None)
    print(df)

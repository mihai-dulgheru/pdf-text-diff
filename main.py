import pandas as pd

from functions import extract_text_from_pdfs, find_text_differences

if __name__ == '__main__':
    file_list = ['template.pdf', 'template_changed.pdf']
    ocr_dic = extract_text_from_pdfs(file_list)
    n = len(file_list)
    d = {'filename': [file_list[i] for i in range(n)],
         'conf': [ocr_dic[file_list[i]]['conf'].values[0] for i in range(n)],
         'text': [ocr_dic[file_list[i]]['text'].values[0] for i in range(n)]}
    df = pd.DataFrame(data=d, index=list(range(n)))
    pd.set_option("display.max_columns", None)
    print()
    print(df)

    diffs = find_text_differences(ocr_dic)
    print()
    print(diffs)

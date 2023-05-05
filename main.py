from functions import extract_text_from_pdfs, find_text_differences, show_details

if __name__ == '__main__':
    file_list = ['template.pdf', 'template_changed.pdf']
    ocr_dic = extract_text_from_pdfs(file_list)
    # show_details(file_list, ocr_dic)
    diffs = find_text_differences(ocr_dic)
    print(diffs)

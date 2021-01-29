# @Copyright(C), OldFive, 2020.
# @Date : 2021/1/21 9:18:07
# @Author : OldFive
# @Version : 0.1
# @Description : 
# @History :
# @Other:
#  ▒█████   ██▓    ▓█████▄   █████▒██▓ ██▒   █▓▓█████
# ▒██▒  ██▒▓██▒    ▒██▀ ██▌▓██   ▒▓██▒▓██░   █▒▓█   ▀
# ▒██░  ██▒▒██░    ░██   █▌▒████ ░▒██▒ ▓██  █▒░▒███
# ▒██   ██░▒██░    ░▓█▄   ▌░▓█▒  ░░██░  ▒██ █░░▒▓█  ▄
# ░ ████▓▒░░██████▒░▒████▓ ░▒█░   ░██░   ▒▀█░  ░▒████▒
# ░ ▒░▒░▒░ ░ ▒░▓  ░ ▒▒▓  ▒  ▒ ░   ░▓     ░ ▐░  ░░ ▒░ ░
#   ░ ▒ ▒░ ░ ░ ▒  ░ ░ ▒  ▒  ░      ▒ ░   ░ ░░   ░ ░  ░
# ░ ░ ░ ▒    ░ ░    ░ ░  ░  ░ ░    ▒ ░     ░░     ░
#     ░ ░      ░  ░   ░            ░        ░     ░  ░
#                   ░                      ░
#
"""
函数主入口
"""

import filetype


def main(file_path):
    kind = filetype.guess(file_path)
    if kind is None:
        print()
        print('Cannot guess file type!')
        print()
        return
    print()
    # print('File extension: %s' % kind.extension)
    # print('File MIME type: %s' % kind.mime)


if __name__ == '__main__':
    main(r'test_file/office1/office_excel_xlsx_1_有文字.xlsx')
    main(r'test_file/wps1/wps_excel_xlsx_1_有文字.xlsx')
    main(r'test_file/office1/office_ppt_pptx_1_有文字.pptx')
    main(r'test_file/wps1/wps_ppt_pptx_1_有文字.pptx')
    main(r'test_file/office1/office_word_docx_1_有文字.docx')
    main(r'test_file/wps1/wps_word_wocx_1_有文字.docx')

from docx import Document

files_name = [
    #r'test_file/office1/office_excel_xlsx_1_有文字.xlsx', r'test_file/wps1/wps_excel_xlsx_1_有文字.xlsx',
    #r'test_file/office1/office_ppt_pptx_1_有文字.pptx', r'test_file/wps1/wps_ppt_pptx_1_有文字.pptx',
              r'test_file/office1/office_word_docx_1_有文字.docx', r'test_file/wps1/wps_word_wocx_1_有文字.docx']
for file_name in files_name:
    doc = Document(file_name)
    for para in doc.paragraphs:
        print(para.text)

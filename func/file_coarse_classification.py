# @Copyright(C), OldFive, 2020.
# @Date : 2021/1/21 0021 10:05:15
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
获取文件列表并解析文件类型
"""

import os
import struct
import filetype


def is_dir(path: str):
    """对传进来的路径进行判断是否为文件夹
    :param path: 路径
    """
    if os.path.isdir(path):
        pass


def typeList():
    return {
        # "FFD8FF": "JPEG",
        "89504E4789504E47": "PNG"}


# 字节码转16进制字符串
def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


# 获取文件类型
def read_file(filename):
    file = open(filename, 'rb')
    file_bytes = file.read(50)
    file_str = ''
    for file_byte in file_bytes:
        file_str += (u"%x" % file_byte).rjust(2, '0')

    # print(file_str, filename)

    # for hcode in tl.keys():
    #     numOfBytes = int(len(hcode) / 2)  # 需要读多少字节
    #     binfile.seek(0)  # 每次读取都要回到文件头，不然会一直往后读取
    #     # print(str(binfile.read(numOfBytes)))
    #     # binfile.seek(0)  # 每次读取都要回到文件头，不然会一直往后读取
    #     # hbytes = struct.unpack_from("B" * numOfBytes, binfile.read(numOfBytes))  # 一个 "B"表示一个字节
    #     print(binfile.read())
    #     hbytes = struct.unpack_from("s", binfile.read())
    #     print(hbytes)
    #     f_hcode = bytes2hex(hbytes)
    #     print(f_hcode)
    #     if f_hcode == hcode:
    #         ftype = tl[hcode]
    #         break
    file.close()
    # return ftype
    return file_str


file_type_flag = {

}


def get_all_file_src(cwd):
    get_dir = os.listdir(cwd)
    for i in get_dir:
        sub_dir = os.path.join(cwd, i)
        if os.path.isdir(sub_dir):
            get_all_file_src(sub_dir)
        else:
            file_str = read_file(os.path.join(cwd, i))
            file_type = os.path.splitext(os.path.join(cwd, i))[1]
            if file_type_flag.__contains__(file_type):
                file_type_flag[file_type].append([file_str, i])
            else:
                file_type_flag[file_type] = [[file_str, i]]


# if __name__ == '__main__':
#     print(read_file(r'../test_file/office1/office_excel_xlsx_1_有文字.xlsx'))
#     # print(read_file(r'../test_file/wps1/wps_excel_xlsx_1_有文字.xlsx'))
#     print(read_file(r'../test_file/office1/office_ppt_pptx_1_有文字.pptx'))
#     # print(read_file(r'../test_file/wps1/wps_ppt_pptx_1_有文字.pptx'))
#     print(read_file(r'../test_file/office1/office_word_docx_1_有文字.docx'))
#     # print(read_file(r'../test_file/wps1/wps_word_wocx_1_有文字.docx'))
#     # get_all_file_src(r'E:\work\GDTSGZ\oldfive\gd_ops_web')
#     # for k, y in file_type_flag.items():
#     #     print(k)
#     #     for yy in y:
#     #         print(yy)


def main():
    kind = filetype.guess('../test_file/wps1/wps_ppt_pptx_1_有文字.pptx')
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)


if __name__ == '__main__':
    main()

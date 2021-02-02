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
from queue import Queue

from func import file_parsing


file_queue = Queue()


def is_dir(path: str):
    """对传进来的路径进行判断是否为文件夹
    :param path: 路径
    """
    if os.path.isdir(path):
        get_all_file(path)
    else:
        get_one_file(path)


def get_one_file(path: str):
    """当路径为单文件时"""
    file_type = os.path.splitext(path)[1]


def get_all_file(path: str):
    """当路径为文件夹时"""
    get_dir = os.listdir(path)
    for i in get_dir:
        sub_dir = os.path.join(path, i)
        if os.path.isdir(sub_dir):
            get_all_file(sub_dir)
        else:
            file_path = os.path.join(path, i)
            file_type = os.path.splitext(os.path.join(path, i))[1]
            file_queue.put((file_path, file_type))


def file_parsing_by_type():
    """多线程读取文件"""
    file_path, file_type = file_queue.get()
    if file_type == 'doc' or file_type == 'docx':
        file_parsing.word_file_parsing(file_path)
    elif file_type == 'xls' or file_type == 'xlsx':
        file_parsing.excel_file_parsing(file_path)



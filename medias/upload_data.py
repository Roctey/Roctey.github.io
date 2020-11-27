import os
import platform
import re
import subprocess
import requests
import json
from loguru import logger


def get_file_name(file_dir):
    if os.path.exists(file_dir):
        for root, dirs, files in os.walk(file_dir):
            # logger.info(f'\n{root}')  # 当前目录路径
            # # logger.info(dirs)  # 当前路径下所有子目录
            # logger.info(f'\n{files}')  # 当前路径下所有非目录子文件
            return root, files
    else:
        logger.info('\n文件夹不存在')
        return [], []
        

def upload_data():
    # logger.add('./log/upload_data_{time}.log', encoding='utf-8')
   
    root, files = get_file_name('./featureimages')
    print(files)
    print(root)
    n = 0
    if files:
        for name in files:
            os.rename(f'./featureimages/{name}', f'./featureimages/{n}.jpg')
            n += 1
    else:
        logger.info('\n没有需要上传的数据')

if __name__ == '__main__':
    upload_data()

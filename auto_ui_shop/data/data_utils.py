import json
import os

# 读取数据文件
def read_test_data(file_path):
    data_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', file_path)
    with open(data_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
import json
import os

# 读取数据文件
def read_test_data():
    data_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'register_data.json')
    with open(data_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
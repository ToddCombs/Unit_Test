# 数据清洗测试脚本
from sqlalchemy import create_engine

server_name = 'rw.etcp_qa.mssql.etcp.cn'
database = 'etcp'
username = 'dev'
password = 'L3XBiv09R+3FBFzr2Njpf6T3x+Gz2LWc'

# 创建引擎
engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server_name}/{database}')


def collection_data():
    """
    存数
    :return:
    """
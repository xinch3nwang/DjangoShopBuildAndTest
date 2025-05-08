import sqlite3

def execute_sql(db_path, sql, params=None):
    """
    执行 SQLite 数据库的 SQL 语句。

    :param db_path: 数据库文件的路径
    :param sql: 要执行的 SQL 语句
    :param params: SQL 语句的参数，默认为 None
    :return: 如果是查询语句，返回查询结果；否则返回 None
    """
    try:
        # 连接到数据库
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        # 如果是查询语句，返回查询结果
        if sql.strip().lower().startswith('select'):
            result = cursor.fetchall()
            return result
        else:
            # 对于非查询语句，提交事务
            conn.commit()
            return None

    except Exception as e:
        print(f"执行 SQL 语句时出错: {e}")
        return None
    finally:
        if conn:
            conn.close()
from db_utils import execute_sql

db_path = r'd:\Code\Personal\DjangoShop\djangoshop\db.sqlite3'
# 显示所有表名
sql = "SELECT name FROM sqlite_master WHERE type='table';"
result = execute_sql(db_path, sql)
print(result)

sql = "SELECT line_price, stock FROM shop_baykeshopgoodssku WHERE id = 1;"
result = execute_sql(db_path, sql)
print(result)
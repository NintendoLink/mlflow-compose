import pymysql
import os
from utils import Log


mysql_user = os.environ.get('MYSQL_USER')
mysql_passwd = os.environ.get('MYSQL_PASSWORD')
mysql_host = "mysql-host"
mysql_port = 3306

# 创建数据库mlflow-test
try:
    log = Log()
    log.logger.info(f"create db,host:{mysql_host},port:{mysql_port}")

    # Get connection & cursor
    conn = pymysql.connect(host=mysql_host,
                           user=mysql_user,
                           password=mysql_passwd,
                           port=mysql_port,
                           charset='utf8mb4')
    cursor = conn.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS mlflow_test"
    # execute sql
    cursor.execute(sql)
except BaseException:
    # todo
    raise
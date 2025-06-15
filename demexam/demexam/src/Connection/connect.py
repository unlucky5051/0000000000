from peewee import *
from pymysql import *
mysql_db = MySQLDatabase('cafe', user='root', host='127.0.0.1', port=3306)


if __name__ == "__main__":
    print(mysql_db.connect())
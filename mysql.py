# -*- coding: UTF-8 -*-

import pymysql

#read all database names
def ReadDatabaseName():
    conn=pymysql.connect(host='localhost',user='root',password='password',charset='utf8mb4')
    sql = "SHOW DATABASES"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data








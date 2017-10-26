# usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb

con = MySQLdb.connect(host="localhost",user="root",passwd="Andreia16",db="Testes")
cursor = con.cursor()

sql = """insert into pessoas
values(2, 'andreia');"""
try:
    cursor.execute(sql)
    con.commit()
except:
    con.rollback()

sql = "select * from pessoas"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        nome = row[1]
        print(str(id) + " " + str(nome))
except:
    print("Error")

con.close()

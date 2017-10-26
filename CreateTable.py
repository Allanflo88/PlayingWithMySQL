# usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb

con = MySQLdb.connect(host="localhost",user="root",passwd="Andreia16",db="Testes")
cursor = con.cursor()

cursor.execute("drop table if exists pessoas")

sql = """create table pessoas(
        id integer,
        nome varchar(20));"""

cursor.execute(sql)

sql = """alter table pessoas
        add constraint primary key(id);"""

cursor.execute(sql)

sql = """insert into pessoas
values(1, 'allan');"""
try:
    cursor.execute(sql)
    con.commit()
except:
    db.rollback()
    
con.close()

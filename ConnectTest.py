# usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb

con = MySQLdb.connect(host="localhost",user="root",passwd="Andreia16",db="Testes")
cursor = con.cursor()
cursor.execute("SELECT id, nome FROM pessoas")
data = cursor.fetchone()
print ("Database version : " + str(data))
con.close()

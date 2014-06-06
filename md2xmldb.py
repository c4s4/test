#!/usr/bin/env python
# encoding: UTF-8

import sqlite3

connection = sqlite3.connect('sweetblog.db')
cursor = connection.cursor()
for index in range(100):
    result = cursor.execute("SELECT text FROM entries WHERE id=%s" % index).fetchone()
    print result

#cursor = connection.cursor()
#cursor.execute("DROP TABLE IF EXISTS user")
#cursor.execute("CREATE TABLE user (id integer, name text)")
#cursor.execute("INSERT INTO user (id, name) VALUES (1, 'TOTO'), (2, 'TATA');")
#connection.commit()
#connection.close()


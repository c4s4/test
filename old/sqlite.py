#!/usr/bin/env python
# encoding: UTF-8

import sqlite3

con = sqlite3.connect(':memory:')

c = con.cursor()
c.execute("DROP TABLE IF EXISTS user")
c.execute("CREATE TABLE user (id integer, name text)")
c.execute("INSERT INTO user (id, name) VALUES (1, 'TOTO'), (2, 'TATA');")
con.commit()
con.close()


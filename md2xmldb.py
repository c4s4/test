#!/usr/bin/env python
# encoding: UTF-8

import sqlite3

QUERY = "SELECT title, text FROM entries WHERE id=%s"
TEMPLATE = '''# id:       %(index)s
# title:    %(title)s
# author:   Michel Casabianca
# email:    michel.casabianca@gmail.com
# keywords: 

%(text)s'''

connection = sqlite3.connect('sweetblog.db')
cursor = connection.cursor()
number = cursor.execute("SELECT count(*) FROM entries").fetchone()[0]
for index in range(number):
    result = cursor.execute(QUERY % index).fetchone()
    if result:
        title = result[0].strip()
        text = result[1].strip()
        params = {
            'index': index,
            'title': title,
            'text':  text,
        }
        open("/tmp/%s.bd" % index, 'wb').write(TEMPLATE % params) 
        print index, title
connection.close()


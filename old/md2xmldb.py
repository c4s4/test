#!/usr/bin/env python
# encoding: UTF-8
# 
# Script to generate beedoc files, with metadata, from sqlite database of the
# sweetblog project.

import codecs
import sqlite3

QUERY = "SELECT date, title, text FROM entries WHERE id=%s"
TEMPLATE = u'''# id:       %(index)s
# date:     %(date)s
# title:    %(title)s
# author:   Michel Casabianca
# email:    michel.casabianca@gmail.com
# keywords: 

%(text)s'''

connection = sqlite3.connect('sweetblog.db')
cursor = connection.cursor()
number = cursor.execute("SELECT count(*) FROM entries").fetchone()[0]
for index in range(number+1):
    result = cursor.execute(QUERY % index).fetchone()
    if result:
        date = result[0].strip()
        title = result[1].strip()
        text = result[2].strip().replace('\r\n', '\n')
        params = {
            'date':  date,
            'index': index,
            'title': title,
            'text':  text,
        }
        document = TEMPLATE % params
        stream = codecs.open("bd/%s.bd" % index, 'wb', encoding='UTF-8')
        stream.write(document) 
        print index, title
        stream.close()
connection.close()


#!/usr/bin/env python
# encoding: UTF-8

import os
import http1

ACTION = 'ORA.PA'
URL = "http://finance.yahoo.com/q?s=%s" % ACTION

def error(message):
    print message
    os.exit(1)

def main():
    response = http1.get(URL)
    if response.status != 200:
        error("Bad status %s" % response.status)
    print response.body

if __name__ == '__main__':
    main()

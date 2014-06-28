#!/usr/bin/env python
# encoding: UTF-8

import sys
import json
import http1

USER = 'c4s4'
URL = "https://api.github.com/users/%s/repos"
HEADERS = {
    'User-Agent': 'casa',
}

def main(user):
    response = http1.get(URL % user, headers=HEADERS)
    if response.status != 200:
        print "Error calling API: %s" % response.body
        sys.exit(1)
    return json.loads(response.body)

if __name__ == '__main__':
    repos = main(USER)
    print repos[0].keys()

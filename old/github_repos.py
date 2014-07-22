#!/usr/bin/env python
# encoding: UTF-8

import sys
import json
import http1

HELP = '''Print project for a given Github user.
Usage: githut_repos [-h] user
-h     to print this help page
user   the github user to print projects for'''
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
    user = USER
    if len(sys.argv) > 2:
        print HELP
        sys.exit(1)
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == '-h' or arg == '--help':
            print HELP
            sys.exit(0)
        else:
            user = arg
    repos = main(user)
    names = sorted([repo['name'] for repo in repos])
    print ' '.join(names)

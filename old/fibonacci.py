#!/usr/bin/env python
# encoding: UTF-8

import sys

if len(sys.argv) > 1:
    x = int(sys.argv[1])
else:
    x = 10

p = 1
n = 1

print p
print n
for i in range(x):
    p, n = (n, n+p)
    print n
print float(n)/p


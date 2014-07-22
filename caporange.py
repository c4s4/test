#!/usr/bin/env python
# encoding: UTF-8

GARANTIES  = 293
CLASSIQUES = 387

#OFFERTES = GARANTIES / 2 + CLASSIQUES / 5
OFFERTES = 146 + 80
TOTAL = GARANTIES + CLASSIQUES + OFFERTES

def afficher():
    print "Actions garanties: %s" % GARANTIES
    print "Actions classiques: %s" % CLASSIQUES
    print "Actions offertes: %s" % OFFERTES
    print "Actions total: %s" % TOTAL

def main():
    afficher()

if __name__ == '__main__':
    main()

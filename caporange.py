#!/usr/bin/env python
# encoding: UTF-8

GARANTIES  = 293
CLASSIQUES = 387

#OFFERTES = GARANTIES / 2 + CLASSIQUES / 5
OFFERTES = 146 + 80
TOTAL = GARANTIES + CLASSIQUES + OFFERTES

PRIX = 9.69

CSG_RDS = OFFERTES * PRIX * 0.08
PAYE = (GARANTIES + CLASSIQUES) * PRIX + CSG_RDS

def afficher():
    print "Actions garanties:  %s" % GARANTIES
    print "Actions classiques: %s" % CLASSIQUES
    print "Actions offertes:   %s" % OFFERTES
    print "Actions total:      %s" % TOTAL
    print "Prix d'achat:       %s" % PRIX
    print "Payé:               %s" % PAYE

def main():
    afficher()

if __name__ == '__main__':
    main()

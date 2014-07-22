#!/usr/bin/env python
# encoding: UTF-8

COURS = 11.63

GARANTIES  = 293
CLASSIQUES = 387

#OFFERTES = GARANTIES / 2 + CLASSIQUES / 5
OFFERTES = 146 + 80
TOTAL = GARANTIES + CLASSIQUES + OFFERTES

PRIX = 9.69
COURS_ACHAT = round(PRIX / 0.8, 2)
CSG_RDS = OFFERTES * PRIX * 0.08
PAYE = round((GARANTIES + CLASSIQUES) * PRIX + CSG_RDS, 2)

VALEUR = round(TOTAL * COURS, 2)
PLUS_VALUE = VALEUR - PAYE

def afficher():
    print "Actions garanties:  %s" % GARANTIES
    print "Actions classiques: %s" % CLASSIQUES
    print "Actions offertes:   %s" % OFFERTES
    print "Actions total:      %s" % TOTAL
    print "Cours d'achat:      %s" % COURS_ACHAT
    print "Prix d'achat:       %s" % PRIX
    print "Payé:               %s" % PAYE
    print "Valeur:             %s" % VALEUR
    print "Plus-value:         %s" % PLUS_VALUE

def main():
    global COURS
    if len(os.argv) > 1:
        COURS = int(os.argv[1])
    afficher()

if __name__ == '__main__':
    main()

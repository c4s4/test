#!/usr/bin/env python
# encoding: UTF-8

import sys
import getopt

prime_numbers = []

def is_prime(number):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    number = long(number)
    # 0 and 1 are not primes
    if number < 2:
        return False
    # 2 is the only even prime number
    if number == 2: 
        return True    
    # all other even numbers are not primes
    if not number & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for div in range(3, int(number**0.5)+1, 2):
        if number % div == 0:
            return False
    return True

def main(number):
    try:
        number = long(number)
        prime = "prime" if is_prime(number) else "not prime"
        print "%s is %s" % (number, prime)
    except Exception:
        print "%s is not a number" % number

# Command line help
HELP = """Usage: %s [-h] number
-h      Print this help page
number  Tells if this number is prime""" % sys.argv[0]

# parse command line
if __name__ == '__main__':
    number = 0
    try:
        OPTS, ARGS = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.GetoptError, error:
        print "ERROR: %s" % str(error)
        print HELP
        sys.exit(1)
    for OPT, ARG in OPTS:
        if OPT == "-h":
            print HELP
            sys.exit(0)
        else:
            print "Unhandled option: %s" % OPT
            print HELP
            sys.exit(1)
    for number in ARGS:
        main(number)


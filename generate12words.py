#!/usr/bin/env python
# encoding: utf-8
"""


#  Bip39 by TheRealLordFractal 2019

"""

import sys
import getopt
import random

#sys.stdout = open('electrum-mnemonic-1626.txt','wt')

help_message = '''
Bip39 12 Word Random Generator By TheRealLordFractal
Output File Saved as 12words.txt
Command Exntensions:
-n <x> or --number <x>: Number of sample code phrases given. (Default is 5)
-w <file> or --wordlist <file>: Uses another wordlist to generate code phrases from.
'''

CODEWORDS = open('wordlist.txt', 'r').readlines()
outputtxt = open('12words.txt', 'w')

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def generate(prefix=False, number=5):
    while number > 0:        
        if prefix == 'TRUE':
           print ("Not Supported.")
           # word1 = PREFIXES[int(random.uniform(0,len(PREFIXES)))]
        elif prefix:
            word1 = prefix
        else:
            word1 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word2 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word3 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word4 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word5 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word6 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word7 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word8 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word9 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word10 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word11 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            word12 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
        print >> outputtxt, " %s %s %s %s %s %s %s %s %s %s %s %s " % (word1.rstrip(), word2.rstrip(), word3.rstrip(), word4.rstrip(), word5.rstrip(), word6.rstrip(), word7.rstrip(), word8.rstrip(), word9.rstrip(), word10.rstrip(), word11.rstrip(), word12.rstrip())
        
        number -= 1
    

def main(argv=None):
    
    number = 5
    prefix = False
    
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hn:p:i:vw:", ["help", "number=", "prefix=", "wordlist="])
        except getopt.error, msg:
            raise Usage(msg)
    
        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-n", "--number"):
                number = int(value)
            if option in ("-w", "--wordlist"):
                global CODEWORDS
                print "Importing: %s" % value
                CODEWORDS = open(value, 'r').readlines()
            if option in ("-p", "--prefixe"):
                
                print value
                
                if (value):
                    prefix = value
                else:
                    prefix = 'TRUE'
    
        generate(prefix, number)
    
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())

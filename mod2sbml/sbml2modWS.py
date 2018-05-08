#!/usr/bin/python
# sbml2modWS.py
# uses BASIS WS for sbml2mod conversion
# can use as a module or a script...

# Darren Wilkinson (d.j.wilkinson@ncl.ac.uk)
# http://www.staff.ncl.ac.uk/d.j.wilkinson/

import sys,SOAPpy

def parse(string):
    ws=SOAPpy.SOAPProxy('https://www.basis.ncl.ac.uk/basis-model')
    return(ws.sbml2mod(string))

def parseFile(file):
    s=open(file,'r')
    string=s.read()
    return(parse(string))

if (__name__=='__main__'):
    if (len(sys.argv)!=2):
        print "Usage: "+sys.argv[0]+" <sbmlFile>"
        sys.exit(1)
    print parseFile(sys.argv[1])

# eof


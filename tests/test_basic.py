# test_basic.py
# some very basic sanity checks

import libsbml
from sbmlsh import *

def test_m2s():
    p = mod2sbml.Parser()
    s = open("mm.mod", "r")
    sb = p.parseStream(s)
    assert(len(sb.toSBML()) > 100)

def test_s2m():
    s = open("mm.xml","r").read()
    d = libsbml.SBMLReader().readSBMLFromString(s)
    p = sbml2mod.Parser(d)
    sh = p.parse()
    assert(len(sh) > 50)


# eof

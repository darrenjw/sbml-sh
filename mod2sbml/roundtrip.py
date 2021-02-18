#!/usr/bin/python
# roundtrip.py

import sys,mod2sbml,sbml2mod

TestFailed="Roundtrip test failure"

def roundtrip(filename):
    # print "Testing "+filename
    try:
        mod=open(filename,"r").read()
    except:
        sys.stderr.write("Error: Failed to open: "+filename+"\n")
        raise IOError
    p1=mod2sbml.Parser()
    sbmld1=p1.parse(mod)
    p2=sbml2mod.Parser(sbmld1)
    backp=p2.parse()
    p3=mod2sbml.Parser()
    sbmld2=p3.parse(backp)
    if (sbmld1.toSBML()==sbmld2.toSBML()):
        print("Roundtrip test passed for "+filename)
    else:
        print("Test FAILED for "+filename)
        raise TestFailed
    
if (__name__=="__main__"):
    for file in sys.argv[1:]:
        try:
            roundtrip(file)
        except IOError:
            sys.stderr.write("IO Error!\n")
            sys.exit(1)
        except TestFailed:
            sys.stderr.write("Test Failure Error!\nPlease report!\n")
            sys.exit(1)
        except:
            sys.stderr.write("Unknown Error!\n")
            sys.exit(1)
    print("\n\nAll tests passed!\n")

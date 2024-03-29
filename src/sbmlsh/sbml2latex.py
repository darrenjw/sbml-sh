#!/usr/bin/env python3
# sbml2latex.py

# Updated: 29/12/23

import sys, io, libsbml

__doc__="""sbml2latex version 1.0

Copyright (C) 2008, Darren J Wilkinson
 d.j.wilkinson@ncl.ac.uk
 http://www.staff.ncl.ac.uk/d.j.wilkinson/

This is GNU Free Software (General Public License)

Module for converting SBML to LaTeX, version 1.0
Typical usage:
>>> from sbml2latex import Parser
>>> p=Parser(sbmldoc)
>>> p.parseStream(sys.stdout)

Raises error "ParseError" on a fatal parsing error.
"""

ParseError="Parsing error"


class Parser(object):
    """Parser class
    Has constructor:
    Parser(sbmldoc)
    where sbmldoc is a libsbml sbmldocument object,
    and the following public methods:
    parseStream(outStream)
    parse()
    """

    def __init__(self,d):
        self.d=d
        self.m=d.getModel()

    def parseStream(self,outS):
        """parseStream(outStream)
        parses SBML model and writes LaTeX to outStream
        """
        outS.write('@model:')
        outS.write(str(self.d.getLevel())+'.')
        outS.write(str(self.d.getVersion())+'.')
        self.mangle=10*self.d.getLevel()+self.d.getVersion()
        outS.write('0='+self.m.getId())
        if (self.m.getName()!=""):
            outS.write(' "'+self.m.getName()+'"')
        outS.write('\n')
        n=self.m.getNumUnitDefinitions()
        if (n>0):
            outS.write('@units\n')
            for i in range(n):
                ud=self.m.getUnitDefinition(i)
                outS.write(' '+ud.getId())
                for j in range(ud.getNumUnits()):
                    if (j==0):
                        outS.write('=')
                    else:
                        outS.write('; ')
                    u=ud.getUnit(j)
                    kind=u.getKind()
                    outS.write(libsbml.UnitKind_toString(kind))
                    e=u.getExponent()
                    m=u.getMultiplier()
                    o=u.getOffset()
                    s=u.getScale()
                    first=True
                    if (e!=1):
                        if first==True:
                            outS.write(':')
                            first=False
                        else:
                            outS.write(',')
                        outS.write('e='+str(e))
                    if (m!=1):
                        if first==True:
                            outS.write(':')
                            first=False
                        else:
                            outS.write(',')
                        outS.write('m='+str(m))
                    if (o!=0):
                        if first==True:
                            outS.write(':')
                            first=False
                        else:
                            outS.write(',')
                        outS.write('o='+str(o))
                    if (s!=0):
                        if first==True:
                            outS.write(':')
                            first=False
                        else:
                            outS.write(',')
                        outS.write('s='+str(s))
                if (ud.isSetName()):
                    outS.write(' "'+ud.getName()+'"')
                outS.write('\n')
        if self.m.getNumCompartments():
            outS.write('@compartments\n')
            for c in self.m.getListOfCompartments():
                outS.write(' '+c.getId())
                if (c.isSetOutside()):
                    outS.write('<'+c.getOutside())
                if (c.isSetSize()):
                    outS.write('='+str(c.getSize()))
                if (c.isSetName()):
                    outS.write(' "'+c.getName()+'"')
                outS.write('\n')
        if self.m.getNumSpecies():
            outS.write('@species\n')
            for s in self.m.getListOfSpecies():
                outS.write(' '+s.getCompartment()+':')
                if (s.isSetInitialConcentration()):
                    outS.write('['+s.getId()+']='+str(s.getInitialConcentration()))
                elif (s.isSetInitialAmount()):
                    outS.write(s.getId()+'='+str(s.getInitialAmount()))
                else:
                    outS.write('['+s.getId()+']='+str(s.getInitialConcentration()))
                if (s.getHasOnlySubstanceUnits()):
                    outS.write('s')
                if (s.getBoundaryCondition()):
                    outS.write('b')
                if (s.getConstant()):
                    outS.write('c')
                if (s.isSetName()):
                    outS.write(' "'+s.getName()+'"')
                outS.write('\n')
        if self.m.getNumParameters():
            outS.write('@parameters\n')
            for p in self.m.getListOfParameters():
                outS.write(' '+p.getId()+'=')
                outS.write(str(p.getValue()))
                if (p.isSetName()):
                    outS.write(' "'+p.getName()+'"')
                outS.write('\n')
        if self.m.getNumRules():
            outS.write('@rules\n')
            for r in self.m.getListOfRules():
                outS.write(' ' + r.getVariable() + ' = ' + r.getFormula())
                outS.write('\n')
        if self.m.getNumReactions():
            outS.write('%%% START Reactions\n')
            outS.write('\\begin{align*}\n')
            for r in self.m.getListOfReactions():
#                if (r.getReversible()):
#                    outS.write('@rr=')
#                else:
#                    outS.write('@r=')
#                outS.write(r.getId())
#                if (r.isSetName()):
#                    outS.write(' "'+r.getName()+'"')
#                outS.write('\n ')
                for j in range(r.getNumReactants()):
                    sr=r.getReactant(j)
                    if (j>0):
                        outS.write('+')
                    sto=sr.getStoichiometry()
                    if (sto!=1):
                        outS.write(str(int(sto)))
                    outS.write('\\mathsf{'+sr.getSpecies().replace('_','\\_')+'}')
                if (r.getReversible()):
                    outS.write(' &\\longleftrightarrow ')
                else:
                    outS.write(' &\\longrightarrow ')
                for j in range(r.getNumProducts()):
                    sr=r.getProduct(j)
                    if (j>0):
                        outS.write('+')
                    sto=sr.getStoichiometry()
                    if (sto!=1):
                        outS.write(str(int(sto)))
                    outS.write('\\mathsf{'+sr.getSpecies().replace('_','\\_')+'}')
                for j in range(r.getNumModifiers()):
                    sr=r.getModifier(j)
                    if (j==0):
                        outS.write(' : ')
                        outS.write('\\mathsf{'+sr.getSpecies().replace('_','\\_')+'}')
                    else:
                        outS.write(', ')
                        outS.write('\\mathsf{'+sr.getSpecies().replace('_','\\_')+'}')
                outS.write(' & \n')
                if (r.isSetKineticLaw()):
                    kl=r.getKineticLaw()
                    outS.write(' \\mathit{rate}&= \\mathit{'+kl.getFormula().replace('*',' \\times ').replace('_','\\_')+'}')
                    for k in range(kl.getNumParameters()):
                        if (k==0):
                            outS.write(' : ')
                        else:
                            outS.write(', ')
                        p=kl.getParameter(k)
                        outS.write(p.getId().replace('_','\\_')+'='+str(p.getValue()))
                outS.write(' \\\\ \n')
            outS.write('\\end{align*}\n')
            outS.write('%%% END Reactions\n')
        if self.m.getNumEvents():
            outS.write('@events\n')
            for e in self.m.getListOfEvents():
                outS.write(" "+e.getId()+"= ")
                trig=e.getTrigger()
                trigger=libsbml.formulaToString(trig.getMath())
                outS.write(trigger)
                if e.isSetDelay():
                    outS.write(' ; ')
                    dmath=e.getDelay()
                    delay=libsbml.formulaToString(dmath.getMath())
                    outS.write(delay)
                outS.write(' : ')
                nea=e.getNumEventAssignments()
                for eai in range(nea):
                    if (eai>0):
                        if (self.mangle>=23):
                            outS.write('; ')
                        else:
                            outS.write(', ')
                    ea=e.getEventAssignment(eai)
                    outS.write(ea.getVariable()+"=")
                    m=ea.getMath()
                    mf=libsbml.formulaToString(m)
                    outS.write(mf)
                if e.isSetName():
                    outS.write(' "'+e.getName()+'"')
                outS.write("\n")


    def parse(self):
        """parse()
Parses the SBML (L2) model and returns a string containing the
corresponding LaTeX"""
        outS=io.StringIO()
        self.parseStream(outS)
        return outS.getvalue()


if __name__=='__main__':
    argc=len(sys.argv)
    try:
        if (argc==1):
            s=sys.stdin
        else:
            try:
                s=open(sys.argv[1],"r")
            except:
                sys.stderr.write('Error: failed to open file: ')
                sys.stderr.write(sys.argv[1]+'\n')
                sys.exit(1)
        string=s.read()
        r=libsbml.SBMLReader()
        d=r.readSBMLFromString(string)
        # print d
        p=Parser(d)
        p.parseStream(sys.stdout)
    except:
        sys.stderr.write('\n\n Unknown parsing error!\n')
        sys.exit(1)


# eof


#!/usr/bin/env python
# sbml-latex-extract.py
# script to extract parts of the output from sbml2latex.py

import sys
startstring='%%% START '
endstring='%%% END '

# TODO: check arguments
part=sys.argv[1]
start=startstring+part
end=endstring+part
s=sys.stdin
o=sys.stdout
# TODO - allow filenames?
line=s.readline()
while (line):
    if line[:-1]==start:
        break
    line=s.readline()
while (line):
    o.write(line)
    if line[:-1]==end:
        break
    line=s.readline()
    



# eof


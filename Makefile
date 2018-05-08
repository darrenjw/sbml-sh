# Makefile


VERSION=3.1.1.1

update:
	svn update
	svn log|less

commit:
	svn commit
	svn update
	svn log|less

docs:
	cd spec ; make
	cd mod2sbml/doc ; make

web:
	make docs
	echo "Installing to version directory $(VERSION)"
	scp spec/sbml-sh.pdf mod2sbml/doc/mod2sbml.pdf mod2sbml/mod2sbml.py mod2sbml/sbml2mod.py @unix.ncl.ac.uk:public_html/software/sbml-sh/$(VERSION)/


# eof


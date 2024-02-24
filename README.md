# sbmlsh - SBML-shorthand

This page describes a "shorthand" version of [SBML](http://sbml.org/)
that is much easier to read and write by hand than real SBML, together
with a software tool that translates the shorthand model description to
real SBML.

It isn't really meant as a complete alternative to GUI model-building
tools. It is just a useful tool for rapid building of essential model
structure. Once the basics are defined, you can translate to SBML and
load up in the GUI tool of your choice.

### Example

The following is a complete description of a simple enzyme-kinetics
model using the shorthand notation.

    @model:2.3.1=MichaelisMentenKinetics "Michaelis-Menten Kinetics"
    @compartments
     cell=1
    @species
     cell:Substrate=1000
     cell:Enzyme=100
     cell:Complex=0
     cell:Product=0
    @parameters
     k1=1
     k1r=2
    @reactions
    @rr=SubstrateEnzymeBinding "Substrate-enzyme binding"
     Substrate+Enzyme -> Complex
     k1*Substrate*Enzyme-k1r*Complex
    @r=Conversion
     Complex -> Product + Enzyme
     k2*Complex : k2=3

You can download this example: [mm.mod](mm.mod). Using the translation
tool below, this model translates to [this SBML](mm.xml).

### Latest SBML-shorthand specification

-   SBML-shorthand specification, version 3.1.1
    ([PDF](spec/sbml-sh.pdf)) - targeted at SBML Level 3, Version 1.

### mod2sbml.py model translation tool

-   [mod2sbml.py](mod2sbml/mod2sbml.py) code and documentation
    ([PDF](doc/mod2sbml.pdf)) (version 3.1.1.1), which is targeted
    at SBML-shorthand version 3.1.1, *and all previous versions*.

Note that this translator is written in
[Python](http://www.python.org/), so you need a working Python
environment including [libSBML](http://www.sbml.org/libsbml.html)
version \>= 5.0.0 and the libSBML Python bindings. See the libSBML
website for information on installing the libSBML python bindings, but
note that on many Linux and similar systems it can be as simple as
installing the `python-libsbml` package with the default OS package
manager.

### sbml2mod.py

-   [sbml2mod.py](mod2sbml/sbml2mod.py) (version 3.1.1.1) is the reverse
    translation tool for Level 3, version 1 and all previous versions.
    It requires libsbml (and the libsbml python bindings).

Obviously, as the shorthand specification does not contain all SBML
features, there is likely to be loss involved. However, there should be
no semantic loss in the round-trip SBML-sh -\> SBML -\> SBML-sh. ie.
doing a `mod2sbml.py` conversion followed by a `sbml2mod.py` conversion
should get back to a shorthand file that is semantically equivalent to
the original. `sbml2mod.py` works very similarly to `mod2sbml.py`, so no
separate documentation should be necessary.

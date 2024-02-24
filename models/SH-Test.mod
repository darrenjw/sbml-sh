@model:3.1.1=MyName "My Model"
 s=substance,t=second,v=litre
@units
 substance=item "item (substance default)"
 mmls=mole:s=-3; litre:e=-1; second:e=-1
@compartments
 cell=1 
 cytoplasm=0.8
 nucleus=0.1
 mito "Mitochondria"
 cell2
@species
 cell:Gene = 10b "The Gene"
 cell:P2=0
 cell:S1=100s
 cell:[S2]=20sc
 cell:[S3]=1000bc
 mito:S4=0b
@parameters
 k1=1  # a comment
 k2 = 10v "K2"
@rules
 PTot = P + 2*P2
 v = 1 + 0.5*t
 @rate:v2=1
@reactions
@r=RepressionBinding "Repression Binding"
 Gene + 2P -> P2Gene
 k2*Gene
@rr=Reverse
 P2Gene -> Gene+2P
 k1r*P2Gene : k1r=1,k2=3
@r=NoKL
 Harry->Jim : Fred
@r=Test
 Fred -> Fred2
 k4*Fred : k4=1
@events
 reset= t>=25 : P=100; P2=0 "Reset event"
 flush= P>10 ; 20 : P=0


@model:3.1.1=MichaelisMentenKinetics "Michaelis-Menten Kinetics"
 s=substance,t=second,v=litre
@units
 substance=item "molecules"
@compartments
 cell
@species
 cell:Substrate=1000 s
 cell:Enzyme=100 s
 cell:Complex=0 s
 cell:Product=0 s
@parameters
 k1=1
 k2=2
 k3=3
@reactions
@r=SubstrateEnzymeBinding "Substrate-enzyme binding"
 Substrate+Enzyme -> Complex
 k1*Substrate*Enzyme
@r=SubstrateEnzymeDissociation "Substrate-enzyme dissociation"
 Complex -> Substrate+Enzyme
 k2*Complex
@r=Conversion
 Complex -> Product + Enzyme
 k3*Complex

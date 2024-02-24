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

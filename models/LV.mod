@model:1.2.1=LotkaVolterraSystem
@compartments
 Cell=1
@species
 Cell:Prey=50
 Cell:Predator=100
@parameters
 a=0.25
 b=0.0025
 c=0.125
@reactions
@r=PreyReproduction
 Prey ->  2Prey
 a*Prey
@r=PredatorReproduction
 Prey + Predator ->  2Predator
 b*Predator*Prey
@r=PredatorDecay
 Predator -> 
 c*Predator

@model:2.4.1=SusceptibleInfectiveRemovedModel
@compartments
 Cell=1
@species
 Cell:S=1000
 Cell:I=5
 Cell:R=0
@parameters
 Lambda=0.001
 Mu=0.1
@reactions
@r=Infection
 S ->  I
 Lambda*S*I
@r=Removal
 I ->  R
 Mu*I
